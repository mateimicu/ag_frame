#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factory that returns all runners fron the project that are finall.
"""
from __future__ import print_function

import importlib

# pylint-disable: wrong-import-order
from ag_frame import exceptions
from ag_frame.runners import base

PREFIX = "ag_frame.runners"
RUNNERS = [
    "run_alg",
]


def runners_factory():
    """Get all runners as a list."""
    all_runners = []
    for runner_module in RUNNERS:
        module_name = "{}.{}".format(PREFIX, runner_module)
        module = importlib.import_module(module_name)
        for item in dir(module):
            item = getattr(module, item)
            try:
                if issubclass(item, base.BaseRunner):
                    item.is_implemented()
                else:
                    continue
            except (exceptions.RunnersNotImplemented, TypeError):
                continue
            all_runners.append(item)

    return all_runners
