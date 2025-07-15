# How to contribute to LINE Bot SDK for Python project

First of all, thank you so much for taking your time to contribute!
LINE Bot SDK for Python is not very different from any other open source projects you are aware of.
It will be amazing if you could help us by doing any of the following:

- File an issue in [the issue tracker](https://github.com/line/line-bot-sdk-python/issues) to report bugs and propose new features and improvements.
- Ask a question using [the issue tracker](https://github.com/line/line-bot-sdk-python/issues) (__Please ask only about this SDK__).
- Contribute your work by sending [a pull request](https://github.com/line/line-bot-sdk-python/pulls).

## Development

### Install dependencies

Run `pip install -r requirements-dev.txt` to install all dependencies for development and testing.

### Understand the project structure

The project structure is as follows:

- `linebot`: The main library code.
- `tests`: Test code.
- `examples`: Example projects that use the library.
- `generator`: Custom OpenAPI generator for Python code.
- `tools`: Development tools.
- `docs`: Documentation files for Sphinx.

### Edit OpenAPI templates

Most of the API client code is generated with OpenAPI Generator based on [line-openapi](https://github.com/line/line-openapi)'s YAML files.
You cannot edit almost all code under `linebot/v3/` directly.

If you need to change the generated code, you should modify the custom templates under:
- `generator/src/main/resources/python-nextgen-custom-client/`

After editing the templates, run `python generate-code.py` to regenerate the code, and then commit all affected files.
If not, CI status will fail.

When you update code, be sure to check consistencies between generated code and your changes.

### Add unit tests

We use [pytest](https://pytest.org/) for unit tests.
Please add tests to the appropriate test directories to verify your changes.

Especially for bug fixes, please follow this flow for testing and development:
1. Write a test before making changes to the library and confirm that the test fails.
2. Modify the code of the library.
3. Run the test again and confirm that it passes thanks to your changes.

### Run your code in your local environment

You can use the [example projects](examples/) to test your changes locally before submitting a pull request.

### Run CI tasks in your local environment

Test by using tox.
To run all tests and to run flake8 against all versions, use: `tox`

To run all tests against version 3.10, use: `tox -e py3.10`

To run a test against version 3.10 and against a specific file, use: `tox -e py3.10 -- tests/test_webhook.py`

### Documentation

If you edit README.rst, you should execute the following command to check the syntax of README.

```
python -m readme_renderer README.rst
```

## Contributor license agreement

When you are sending a pull request and it's a non-trivial change beyond fixing typos, please make sure to sign
[the ICLA (individual contributor license agreement)](https://cla-assistant.io/line/line-bot-sdk-python). Please
[contact us](mailto:dl_oss_dev@linecorp.com) if you need the CCLA (corporate contributor license agreement).
