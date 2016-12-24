#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factory that returns all the algorithms fron the project that are finall.
"""
from __future__ import print_function

import importlib

# pylint-disable: wrong-import-order
from ag_frame.algorithms.representations import base
from ag_frame import exceptions

PREFIX = "ag_frame.algorithms.representations"
REPRESENTAIONS = [
    "bit_array",
]


def representations_factory():
    """Get all representations as a list."""
    all_reprs = []
    for repr_module in REPRESENTAIONS:
        module_name = "{}.{}".format(PREFIX, repr_module)
        module = importlib.import_module(module_name)
        for item in dir(module):
            item = getattr(module, item)
            try:
                if issubclass(item, base.BaseRepresentation):
                    item.is_implemented()
                else:
                    continue
            except (exceptions.RepresentationNotImplemented, TypeError):
                continue

            all_reprs.append(item)

    return all_reprs
