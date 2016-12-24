#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factory that returns all the algorithms fron the project that are finall.
"""
from __future__ import print_function

import importlib

# pylint-disable: wrong-import-order
from ag_frame.algorithms.representations.crossovers import base
from ag_frame import exceptions

PREFIX = "ag_frame.algorithms.representations.crossovers"
CROSSOVERS = [
    "bit_cut",
    "bit_flip",
]


def crossover_factory():
    """Get all representations as a list."""
    all_crossovers = []
    for crossover_module in CROSSOVERS:
        module_name = "{}.{}".format(PREFIX, crossover_module)
        module = importlib.import_module(module_name)
        for item in dir(module):
            item = getattr(module, item)
            try:
                if issubclass(item, base.BaseCrossover):
                    item.is_implemented()
                else:
                    continue
            except (exceptions.CrossoverNotImplemented, TypeError):
                continue

            all_crossovers.append(item)

    return all_crossovers
