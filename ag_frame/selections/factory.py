#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factory that returns all the selections fron the project that are finall.
"""
from __future__ import print_function

import importlib

# pylint-disable: wrong-import-order
from ag_frame.selections import base
from ag_frame import exceptions

PREFIX = "ag_frame.selections"
SELECTIONS = [
    "roata_norocului",
    "turneu",
]


def selection_factory():
    """Get all selection as a list."""
    all_selections = []
    for selection_module in SELECTIONS:
        module_name = "{}.{}".format(PREFIX, selection_module)
        module = importlib.import_module(module_name)
        for item in dir(module):
            item = getattr(module, item)
            try:
                if issubclass(item, base.BaseSelection):
                    item.is_implemented()
                else:
                    continue
            except (exceptions.SelectionNotImplemented, TypeError):
                continue

            all_selections.append(item)

    return all_selections
