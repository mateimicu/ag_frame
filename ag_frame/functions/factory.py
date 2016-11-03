#!/usr/bin/env python
"""
Factory that returns all functions fron the project that are finall.
"""
from __future__ import print_function

import importlib

# pylint-disable: wrong-import-order
from ag_frame import exceptions
from ag_frame.functions import base

PREFIX = "ag_frame.functions"
FUNCTIONS = [
]


def functions_factory():
    """Get all functions as a list."""
    all_functions = []
    for function_module in FUNCTIONS:
        module_name = "{}.{}".format(PREFIX, function_module)
        module = importlib.import_module(module_name)
        for item in dir(module):
            item = getattr(module, item)
            try:
                if issubclass(item, base.Function):
                    print("We got in ", item)
                    item.is_implemented()
            except (exceptions.FunctionNotImplemented, TypeError):
                continue

            all_functions.append(item)

    return all_functions
