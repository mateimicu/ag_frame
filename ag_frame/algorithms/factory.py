#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factory that returns all the algorithms fron the project that are finall.
"""
from __future__ import print_function

import importlib

# pylint-disable: wrong-import-order
from ag_frame.algorithms import base
from ag_frame import exceptions

PREFIX = "ag_frame.algorithms"
ALGORITHMS = [
    "rmhc",
    "nahc",
    "sahc",
    "sa",
]


def algorithms_factory():
    """Get all algorithms as a list."""
    all_algorithms = []
    for algorithm_module in ALGORITHMS:
        module_name = "{}.{}".format(PREFIX, algorithm_module)
        module = importlib.import_module(module_name)
        for item in dir(module):
            item = getattr(module, item)
            try:
                if issubclass(item, base.Algorithm):
                    item.is_implemented()
                else:
                    continue
            except (exceptions.AlgorithmsNotImplemented, TypeError):
                continue

            all_algorithms.append(item)

    return all_algorithms
