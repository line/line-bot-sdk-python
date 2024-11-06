import pkgutil
import importlib
import linebot

def import_all_modules(package):
    for importer, modname, ispkg in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
        try:
            importlib.import_module(modname)
            print(f'Successfully imported {modname}')
        except ImportError as e:
            print(f'Failed to import {modname}: {e}')
            raise

import_all_modules(my_library_name)
