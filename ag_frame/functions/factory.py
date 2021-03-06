#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    "griewangks_function",
    "rastrigins_function",
    "rosenbrocks_valley",
    "six_hump_camel_back_function",
    "tema_1_prim_function",
    "supervisor_function",
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
                    item.is_implemented()
                else:
                    continue
            except (exceptions.FunctionNotImplemented, TypeError):
                continue

            all_functions.append(item)

    return all_functions
