#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from ag_frame.algorithms import factory as a_factory
from ag_frame.functions import factory as f_factory
from ag_frame.runners import run_alg

import argparse


def prepare_parser():
    """Prepare the argument parser."""
    parser = argparse.ArgumentParser()
    return parser


def main():
    """The main function for this mini-framework."""
    parser = prepare_parser()
    subparsers = parser.add_subparsers(help="Choose a runner.")
    algorithms = a_factory.algorithms_factory()
    functions = f_factory.functions_factory()

    base_runner = run_alg.RunAlgorithm(parser, subparsers,
                                       algorithms, functions)
    base_runner.evaluate()
