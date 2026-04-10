"""Generate unified LineBotClient and AsyncLineBotClient classes.

This script parses all individual API client classes using the ast module
and generates unified client classes that delegate to the underlying clients.

Client definitions are **auto-discovered** from the generated code so that
adding a new API module requires zero changes to this script.

Run after generate-code.py:
    python3 tools/generate_unified_client.py
"""

import ast
import os
import re
import sys
from dataclasses import dataclass


# Modules to exclude from the unified client.
# - oauth: token management is done before client creation
# - webhooks: models-only module, no real API client
EXCLUDE_MODULES = frozenset({"oauth", "webhooks"})


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class ClientDef:
    """Definition of a single API client to include in the unified client."""
    module: str           # e.g. "messaging"
    sync_file: str        # path relative to repo root
    sync_class: str       # e.g. "MessagingApi"
    async_file: str
    async_class: str      # e.g. "AsyncMessagingApi"
    attr_name: str        # attribute name on unified client, e.g. "_messaging_api"
    base_url: str         # e.g. "https://api.line.me"


@dataclass
class MethodInfo:
    """Extracted information about a public API method."""
    name: str
    params_source: str   # parameter list source (excluding ``self``)
    return_annotation: str  # return type as source text
    docstring: str | None


# ---------------------------------------------------------------------------
# Auto-Discovery
# ---------------------------------------------------------------------------

def discover_clients(repo_root: str) -> list[ClientDef]:
    """Auto-discover API client classes from generated code under ``linebot/v3/``.

    Scans each module directory for sync/async API file pairs, parses them
    with AST to extract class names and base URLs.
    """
    v3_dir = os.path.join(repo_root, "linebot", "v3")
    clients: list[ClientDef] = []

    for module_name in sorted(os.listdir(v3_dir)):
        if module_name.startswith("_") or module_name in EXCLUDE_MODULES:
            continue
        module_dir = os.path.join(v3_dir, module_name)
        api_dir = os.path.join(module_dir, "api")
        if not os.path.isdir(api_dir):
            continue
        # Must have configuration.py to be a proper API module
        if not os.path.isfile(os.path.join(module_dir, "configuration.py")):
            continue

        for filename in sorted(os.listdir(api_dir)):
            if not filename.endswith(".py"):
                continue
            # Skip async files (handled as counterparts) and __init__.py
            if filename.startswith("async_") or filename == "__init__.py":
                continue

            sync_path = os.path.join(api_dir, filename)
            result = _parse_api_file(sync_path)
            if result is None:
                continue
            sync_class, base_url = result

            # Find async counterpart: async_{filename}
            async_path = os.path.join(api_dir, f"async_{filename}")
            if not os.path.isfile(async_path):
                continue
            async_result = _parse_api_file(async_path)
            if async_result is None:
                continue
            async_class = async_result[0]

            attr_name = "_" + _camel_to_snake(sync_class)

            clients.append(ClientDef(
                module=module_name,
                sync_file=os.path.relpath(sync_path, repo_root),
                sync_class=sync_class,
                async_file=os.path.relpath(async_path, repo_root),
                async_class=async_class,
                attr_name=attr_name,
                base_url=base_url,
            ))

    return clients


def _parse_api_file(filepath: str) -> tuple[str, str] | None:
    """Parse an API source file and extract the main class name and base URL.

    Looks for a class with ``self.line_base_path = "..."`` in its ``__init__``.
    Returns ``(class_name, base_url)`` or ``None``.
    """
    with open(filepath, "r") as f:
        source = f.read()

    tree = ast.parse(source)

    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        for item in node.body:
            if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if item.name != "__init__":
                continue
            for stmt in ast.walk(item):
                if not isinstance(stmt, ast.Assign):
                    continue
                for target in stmt.targets:
                    if (isinstance(target, ast.Attribute)
                            and isinstance(target.value, ast.Name)
                            and target.value.id == "self"
                            and target.attr == "line_base_path"
                            and isinstance(stmt.value, ast.Constant)
                            and isinstance(stmt.value.value, str)):
                        return (node.name, stmt.value.value)

    return None


def _camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case.

    ``MessagingApiBlob`` -> ``messaging_api_blob``
    """
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s1).lower()


def _module_alias(module_name: str) -> str:
    """Derive a PascalCase prefix from a module directory name for import aliases.

    ``messaging`` -> ``Messaging``, ``moduleattach`` -> ``Moduleattach``.
    """
    return module_name[0].upper() + module_name[1:]


# ---------------------------------------------------------------------------
# AST Method Extraction
# ---------------------------------------------------------------------------

def _extract_params_source(func: ast.FunctionDef) -> str:
    """Extract parameters source (without ``self``) from a function def."""
    parts: list[str] = []
    args = func.args

    all_args = args.args[1:]  # skip self
    num_defaults = len(args.defaults)
    num_args = len(all_args)

    for i, arg in enumerate(all_args):
        part = arg.arg
        if arg.annotation:
            part += " : " + ast.unparse(arg.annotation)
        default_index = i - (num_args - num_defaults)
        if default_index >= 0:
            part += " = " + ast.unparse(args.defaults[default_index])
        parts.append(part)

    if args.vararg:
        parts.append("*" + args.vararg.arg)
    if args.kwarg:
        parts.append("**" + args.kwarg.arg)

    return ", ".join(parts)


def _is_deprecation_wrapper(func_node: ast.FunctionDef) -> bool:
    """Return True if the method body contains ``warnings.warn(..., DeprecationWarning)``."""
    for node in ast.walk(func_node):
        if not isinstance(node, ast.Call):
            continue
        if (isinstance(node.func, ast.Attribute)
                and node.func.attr == "warn"
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "warnings"):
            for arg in node.args:
                if isinstance(arg, ast.Name) and arg.id == "DeprecationWarning":
                    return True
    return False


def extract_methods(filepath: str, class_name: str) -> list[MethodInfo]:
    """Parse a Python source file and extract public methods from the given class."""
    with open(filepath, "r") as f:
        source = f.read()

    tree = ast.parse(source)

    target_class: ast.ClassDef | None = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            target_class = node
            break

    if target_class is None:
        raise ValueError(f"Class {class_name} not found in {filepath}")

    methods: list[MethodInfo] = []
    for item in target_class.body:
        if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue

        name = item.name

        # Skip private / dunder methods
        if name.startswith("_"):
            continue

        # Skip @overload stubs (async files have these)
        if any(
            (isinstance(dec, ast.Name) and dec.id == "overload")
            or (isinstance(dec, ast.Attribute) and dec.attr == "overload")
            for dec in item.decorator_list
        ):
            continue

        # Skip deprecation wrappers (e.g. liff backward-compat aliases)
        if _is_deprecation_wrapper(item):
            continue

        params_source = _extract_params_source(item)

        ret_ann = ""
        if item.returns:
            ret_ann = ast.unparse(item.returns)

        methods.append(MethodInfo(
            name=name,
            params_source=params_source,
            return_annotation=ret_ann,
            docstring=ast.get_docstring(item),
        ))

    return methods


# ---------------------------------------------------------------------------
# Import Collection
# ---------------------------------------------------------------------------

def collect_model_imports(filepath: str) -> list[str]:
    """Collect ``from linebot.v3.*.models.* import *`` lines from a source file."""
    imports: list[str] = []
    with open(filepath, "r") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("from linebot.v3.") and ".models." in stripped:
                imports.append(stripped)
    return imports


def collect_typed_imports(filepath: str) -> dict[str, set[str]]:
    """Collect typing / pydantic import names, grouped by source module."""
    result: dict[str, set[str]] = {}
    with open(filepath, "r") as f:
        for line in f:
            stripped = line.strip()
            for prefix in ("from typing_extensions import ",
                           "from typing import ",
                           "from pydantic.v1 import "):
                if stripped.startswith(prefix):
                    module = prefix.replace("from ", "").replace(" import ", "").strip()
                    after_import = stripped[len(prefix):]
                    names = result.setdefault(module, set())
                    for name in after_import.split(","):
                        name = name.strip().rstrip(")").split("#")[0].strip()
                        if name:
                            names.add(name)
                    break
    return result


# ---------------------------------------------------------------------------
# Code Generation Helpers
# ---------------------------------------------------------------------------

def _format_docstring(docstring: str, indent: str = '        ') -> list[str]:
    """Format a multi-line docstring for embedding in generated code.

    The *docstring* is expected to be the already-cleaned output of
    ``ast.get_docstring()`` (leading/trailing blank lines stripped,
    common indent removed).
    """
    if not docstring:
        return []

    doc_lines = docstring.split('\n')
    if len(doc_lines) == 1:
        return [f'{indent}"""{doc_lines[0]}"""']

    result: list[str] = []
    result.append(f'{indent}"""{doc_lines[0]}')
    for line in doc_lines[1:]:
        if line.strip():
            result.append(f'{indent}{line}')
        else:
            result.append('')
    result.append(f'{indent}"""')
    return result


def _extract_call_args_from_params(params_source: str) -> str:
    """Extract call argument names from a parameter source string.

    ``'req : Request, key : Optional[str] = None, **kwargs'``
    -> ``'req, key, **kwargs'``
    """
    if not params_source:
        return ""

    parts: list[str] = []
    depth = 0
    current = ""
    for ch in params_source + ",":
        if ch in "([{":
            depth += 1
            current += ch
        elif ch in ")]}":
            depth -= 1
            current += ch
        elif ch == "," and depth == 0:
            param = current.strip()
            if param:
                if param.startswith("**"):
                    parts.append(param.split()[0])
                elif param.startswith("*"):
                    parts.append(param.split()[0])
                else:
                    name = param.split(":")[0].split("=")[0].strip()
                    parts.append(name)
            current = ""
        else:
            current += ch

    return ", ".join(parts)


# ---------------------------------------------------------------------------
# Code Generation
# ---------------------------------------------------------------------------

def generate_sync_client(
    repo_root: str,
    client_defs: list[ClientDef],
    unique_modules: list[str],
) -> None:
    """Generate ``linebot/v3/line_bot_client.py``."""

    all_model_imports: set[str] = set()
    all_typed_imports: dict[str, set[str]] = {}
    all_methods: list[tuple[ClientDef, MethodInfo, str]] = []

    for cdef in client_defs:
        filepath = os.path.join(repo_root, cdef.sync_file)
        all_model_imports.update(collect_model_imports(filepath))
        for mod, names in collect_typed_imports(filepath).items():
            all_typed_imports.setdefault(mod, set()).update(names)

        methods = extract_methods(filepath, cdef.sync_class)
        for m in methods:
            call_args = _extract_call_args_from_params(m.params_source)
            all_methods.append((cdef, m, call_args))

    # Check for duplicate method names
    seen: set[str] = set()
    for _, m, _ in all_methods:
        if m.name in seen:
            print(f"WARNING: Duplicate method name: {m.name}", file=sys.stderr)
        seen.add(m.name)

    lines: list[str] = []
    lines.append('# coding: utf-8')
    lines.append('')
    lines.append('"""LINE Bot Client.')
    lines.append('')
    lines.append('Auto-generated by tools/generate_unified_client.py.')
    lines.append('Do not edit manually.')
    lines.append('"""')
    lines.append('')

    # Typing / pydantic imports
    for mod in ("typing", "typing_extensions", "pydantic.v1"):
        names = all_typed_imports.get(mod, set())
        if mod == "typing":
            names = names | {"Any", "Optional"}
        if names:
            lines.append(f'from {mod} import {", ".join(sorted(names))}')
    lines.append('')

    # Configuration and ApiClient imports with aliases
    for mod in unique_modules:
        alias = _module_alias(mod)
        lines.append(
            f'from linebot.v3.{mod}.configuration import Configuration as {alias}Configuration'
        )
        lines.append(
            f'from linebot.v3.{mod}.api_client import ApiClient as {alias}ApiClient'
        )
    lines.append('')

    # API class imports
    for cdef in client_defs:
        pkg = cdef.sync_file.replace("/", ".").replace(".py", "")
        lines.append(f'from {pkg} import {cdef.sync_class}')
    # ApiResponse (identical across modules — import from first discovered)
    lines.append(f'from linebot.v3.{unique_modules[0]}.api_response import ApiResponse')
    lines.append('')

    # Model imports (sorted, deduplicated)
    for imp in sorted(all_model_imports):
        lines.append(imp)
    lines.append('')
    lines.append('')

    # ---- class body ----
    lines.append('class LineBotClient:')
    lines.append('    """A single entry-point client that wraps all LINE API operations.')
    lines.append('')
    lines.append('    The LINE Bot SDK v3 splits API operations across multiple subpackages')
    lines.append('    (messaging, audience, insight, liff, etc.), each with its own')
    lines.append('    ``Configuration``, ``ApiClient``, and API class.')
    lines.append('    ``LineBotClient`` consolidates them so that you can call every')
    lines.append('    API method through one instance with a single ``channel_access_token``.')
    lines.append('')
    mod_list = ", ".join(f"``{m}``" for m in unique_modules)
    lines.append(f'    Wrapped subpackages: {mod_list}.')
    lines.append('')
    lines.append('    Auto-generated by ``tools/generate_unified_client.py``.')
    lines.append('    Do not edit manually.')
    lines.append('')
    lines.append('    Usage::')
    lines.append('')
    lines.append('        from linebot.v3 import LineBotClient')
    lines.append('')
    lines.append('        with LineBotClient(channel_access_token="YOUR_TOKEN") as client:')
    lines.append('            client.reply_message(...)')
    lines.append('    """')
    lines.append('')

    # __init__
    lines.append('    def __init__(self, channel_access_token: str, **kwargs) -> None:')
    lines.append('        """Create a unified LINE Bot client.')
    lines.append('')
    lines.append('        :param str channel_access_token: Channel access token.')
    lines.append('        :param kwargs: Additional keyword arguments passed to each Configuration.')
    lines.append('        """')

    for mod in unique_modules:
        alias = _module_alias(mod)
        lines.append(f'        self._{mod}_configuration = {alias}Configuration(')
        lines.append(f'            access_token=channel_access_token, **kwargs')
        lines.append(f'        )')
        lines.append(f'        self._{mod}_api_client = {alias}ApiClient(')
        lines.append(f'            self._{mod}_configuration')
        lines.append(f'        )')
    lines.append('')

    for cdef in client_defs:
        lines.append(
            f'        self.{cdef.attr_name} = {cdef.sync_class}(self._{cdef.module}_api_client)'
        )
    lines.append('')

    # Context manager
    lines.append('    def __enter__(self):')
    lines.append('        return self')
    lines.append('')
    lines.append('    def __exit__(self, exc_type, exc_value, traceback):')
    lines.append('        self.close()')
    lines.append('')
    lines.append('    def close(self) -> None:')
    lines.append('        """Close all underlying API clients."""')
    for mod in unique_modules:
        lines.append(f'        self._{mod}_api_client.close()')
    lines.append('')

    # Delegating methods
    for cdef, method, call_args in all_methods:
        ret_part = f' -> {method.return_annotation}' if method.return_annotation else ''
        if method.params_source:
            sig = f'    def {method.name}(self, {method.params_source}){ret_part}:'
        else:
            sig = f'    def {method.name}(self, **kwargs){ret_part}:'
        lines.append(sig)

        if method.docstring:
            lines.extend(_format_docstring(method.docstring))
        lines.append(f'        return self.{cdef.attr_name}.{method.name}({call_args})')
        lines.append('')

    output_path = os.path.join(repo_root, "linebot/v3/line_bot_client.py")
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    print(f"Generated {output_path} ({len(all_methods)} methods)")


def generate_async_client(
    repo_root: str,
    client_defs: list[ClientDef],
    unique_modules: list[str],
) -> None:
    """Generate ``linebot/v3/async_line_bot_client.py``."""

    all_model_imports: set[str] = set()
    all_typed_imports: dict[str, set[str]] = {}
    all_methods: list[tuple[ClientDef, MethodInfo, str]] = []

    for cdef in client_defs:
        filepath = os.path.join(repo_root, cdef.async_file)
        all_model_imports.update(collect_model_imports(filepath))
        for mod, names in collect_typed_imports(filepath).items():
            all_typed_imports.setdefault(mod, set()).update(names)

        methods = extract_methods(filepath, cdef.async_class)
        for m in methods:
            call_args = _extract_call_args_from_params(m.params_source)
            all_methods.append((cdef, m, call_args))

    lines: list[str] = []
    lines.append('# coding: utf-8')
    lines.append('')
    lines.append('"""Async LINE Bot Client.')
    lines.append('')
    lines.append('Auto-generated by tools/generate_unified_client.py.')
    lines.append('Do not edit manually.')
    lines.append('"""')
    lines.append('')

    # Typing / pydantic imports
    for mod in ("typing", "typing_extensions", "pydantic.v1"):
        names = all_typed_imports.get(mod, set())
        if mod == "typing":
            names = names | {"Any", "Awaitable", "Optional", "Union"}
        if names:
            lines.append(f'from {mod} import {", ".join(sorted(names))}')
    lines.append('')

    # Configuration and AsyncApiClient imports with aliases
    for mod in unique_modules:
        alias = _module_alias(mod)
        lines.append(
            f'from linebot.v3.{mod}.configuration import Configuration as {alias}Configuration'
        )
        lines.append(
            f'from linebot.v3.{mod}.async_api_client import AsyncApiClient as {alias}AsyncApiClient'
        )
    lines.append('')

    # Async API class imports
    for cdef in client_defs:
        pkg = cdef.async_file.replace("/", ".").replace(".py", "")
        lines.append(f'from {pkg} import {cdef.async_class}')
    lines.append(f'from linebot.v3.{unique_modules[0]}.api_response import ApiResponse')
    lines.append('')

    # Model imports
    for imp in sorted(all_model_imports):
        lines.append(imp)
    lines.append('')
    lines.append('')

    # ---- class body ----
    lines.append('class AsyncLineBotClient:')
    lines.append('    """Async version of :class:`LineBotClient`.')
    lines.append('')
    lines.append('    Wraps all LINE API subpackages into a single async client so that')
    lines.append('    every API method can be called through one instance.')
    lines.append('    See :class:`LineBotClient` for details.')
    lines.append('')
    lines.append('    Auto-generated by ``tools/generate_unified_client.py``.')
    lines.append('    Do not edit manually.')
    lines.append('')
    lines.append('    Usage::')
    lines.append('')
    lines.append('        from linebot.v3 import AsyncLineBotClient')
    lines.append('')
    lines.append('        async with AsyncLineBotClient(channel_access_token="YOUR_TOKEN") as client:')
    lines.append('            await client.reply_message(...)')
    lines.append('    """')
    lines.append('')

    # __init__
    lines.append('    def __init__(self, channel_access_token: str, **kwargs) -> None:')
    lines.append('        """Create a unified async LINE Bot client.')
    lines.append('')
    lines.append('        :param str channel_access_token: Channel access token.')
    lines.append('        :param kwargs: Additional keyword arguments passed to each Configuration.')
    lines.append('        """')

    for mod in unique_modules:
        alias = _module_alias(mod)
        lines.append(f'        self._{mod}_configuration = {alias}Configuration(')
        lines.append(f'            access_token=channel_access_token, **kwargs')
        lines.append(f'        )')
        lines.append(f'        self._{mod}_api_client = {alias}AsyncApiClient(')
        lines.append(f'            self._{mod}_configuration')
        lines.append(f'        )')
    lines.append('')

    for cdef in client_defs:
        lines.append(
            f'        self.{cdef.attr_name} = {cdef.async_class}(self._{cdef.module}_api_client)'
        )
    lines.append('')

    # Async context manager
    lines.append('    async def __aenter__(self):')
    lines.append('        return self')
    lines.append('')
    lines.append('    async def __aexit__(self, exc_type, exc_value, traceback):')
    lines.append('        await self.close()')
    lines.append('')

    # Sync context manager (AsyncApiClient also supports it)
    lines.append('    def __enter__(self):')
    lines.append('        return self')
    lines.append('')
    lines.append('    def __exit__(self, exc_type, exc_value, traceback):')
    lines.append('        self.close_sync()')
    lines.append('')

    lines.append('    async def close(self) -> None:')
    lines.append('        """Close all underlying async API clients."""')
    for mod in unique_modules:
        lines.append(f'        await self._{mod}_api_client.close()')
    lines.append('')

    lines.append('    def close_sync(self) -> None:')
    lines.append('        """Synchronously close all underlying async API clients (best-effort)."""')
    for mod in unique_modules:
        lines.append(f'        self._{mod}_api_client.__exit__(None, None, None)')
    lines.append('')

    # Delegating methods — async client methods are actually ``def`` (not ``async def``).
    # They return ``Union[T, Awaitable[T]]``.  We delegate as-is.
    for cdef, method, call_args in all_methods:
        ret_part = f' -> {method.return_annotation}' if method.return_annotation else ''
        if method.params_source:
            sig = f'    def {method.name}(self, {method.params_source}){ret_part}:'
        else:
            sig = f'    def {method.name}(self, **kwargs){ret_part}:'
        lines.append(sig)

        if method.docstring:
            lines.extend(_format_docstring(method.docstring))
        lines.append(f'        return self.{cdef.attr_name}.{method.name}({call_args})')
        lines.append('')

    output_path = os.path.join(repo_root, "linebot/v3/async_line_bot_client.py")
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    print(f"Generated {output_path} ({len(all_methods)} methods)")


def inject_docstring_references(
    repo_root: str,
    client_defs: list[ClientDef],
) -> None:
    """Insert a ``.. tip::`` reference to the unified client in each wrapped class's docstring."""

    # The class docstring in every generated API file ends with:
    #     Do not edit the class manually.
    #     """
    # (4-space indent distinguishes it from the module-level docstring whose
    #  closing ``"""`` sits at column 0.)
    OLD_TAIL = '    Do not edit the class manually.\n    """'

    def _build_new_tail(unified_class: str) -> str:
        return (
            '    Do not edit the class manually.\n'
            '\n'
            f'    Tip: Use :class:`linebot.v3.{unified_class}` to call every\n'
            '    LINE API method through a single instance.\n'
            '    """'
        )

    count = 0
    processed: set[str] = set()
    for cdef in client_defs:
        for filepath, unified in (
            (os.path.join(repo_root, cdef.sync_file), "LineBotClient"),
            (os.path.join(repo_root, cdef.async_file), "AsyncLineBotClient"),
        ):
            if filepath in processed:
                continue
            processed.add(filepath)

            with open(filepath, "r") as f:
                content = f.read()

            new_tail = _build_new_tail(unified)

            # Idempotency: already injected
            if new_tail in content:
                continue

            if OLD_TAIL not in content:
                print(f"WARNING: docstring pattern not found in {filepath}",
                      file=sys.stderr)
                continue

            # Replace only the first occurrence (the class docstring)
            content = content.replace(OLD_TAIL, new_tail, 1)
            with open(filepath, "w") as f:
                f.write(content)
            count += 1

    print(f"Injected unified-client references into {count} files")





def update_init_file(repo_root: str) -> None:
    """Add LineBotClient and AsyncLineBotClient exports to ``linebot/v3/__init__.py``."""
    init_path = os.path.join(repo_root, "linebot/v3/__init__.py")
    with open(init_path, "r") as f:
        content = f.read()

    sync_import = "from .line_bot_client import LineBotClient  # noqa"
    async_import = "from .async_line_bot_client import AsyncLineBotClient  # noqa"

    if sync_import in content:
        return

    with open(init_path, "a") as f:
        f.write(f"\n{sync_import}\n{async_import}\n")

    print(f"Updated {init_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    if not os.path.exists(os.path.join(repo_root, "linebot/v3/__init__.py")):
        print("Error: Cannot find linebot/v3/__init__.py. "
              "Run this script from the repository root or the tools/ directory.",
              file=sys.stderr)
        sys.exit(1)

    client_defs = discover_clients(repo_root)
    unique_modules = list(dict.fromkeys(c.module for c in client_defs))

    print(f"Discovered {len(client_defs)} API clients across "
          f"{len(unique_modules)} modules:")
    for cdef in client_defs:
        print(f"  {cdef.module}: {cdef.sync_class} / {cdef.async_class}")

    generate_sync_client(repo_root, client_defs, unique_modules)
    generate_async_client(repo_root, client_defs, unique_modules)
    inject_docstring_references(repo_root, client_defs)
    update_init_file(repo_root)

    print("Done.")


if __name__ == "__main__":
    main()
