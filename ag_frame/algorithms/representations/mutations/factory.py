#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factory that returns all the algorithms fron the project that are finall.
"""
from __future__ import print_function

import importlib

# pylint-disable: wrong-import-order
from ag_frame.algorithms.representations.mutations import base
from ag_frame import exceptions

PREFIX = "ag_frame.algorithms.representations.mutations"
MUTATIONS = [
    "bit_mutate",
]


def mutation_factory():
    """Get all mutations as a list."""
    all_mutations = []
    for mutation_module in MUTATIONS:
        module_name = "{}.{}".format(PREFIX, mutation_module)
        module = importlib.import_module(module_name)
        for item in dir(module):
            item = getattr(module, item)
            try:
                if issubclass(item, base.BaseMutation):
                    item.is_implemented()
                else:
                    continue
            except (exceptions.MutationNotImplemented, TypeError):
                continue

            all_mutations.append(item)

    return all_mutations
