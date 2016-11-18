#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from ag_frame.algorithms import factory as a_facotry
from ag_frame.functions import factory as f_factory

import argparse


def prepare_parser():
    """Prepare the argument parser."""
    parser = argparse.ArgumentParser()
    return parser


def add_subparsers(base, elements, functions):
    """Add the subparsers."""
    for element in elements:
        element.add_parser(base, functions)


def main():
    """The main function for this mini-framework."""
    parser = prepare_parser()
    subparsers = parser.add_subparsers(help="Run this function as you want.",
                                       dest="alg")
    algorithms = a_facotry.algorithms_factory()
    functions = f_factory.functions_factory()
    add_subparsers(subparsers, algorithms, functions)

    # parser args
    args = parser.parse_args()
    for item in algorithms + functions:
        item._args = args

    # choose algorithm and function
    algorithm = None
    function = None
    for alg in algorithms:
        if alg.name() == args.alg:
            algorithm = alg()
            break
    for func in functions:
        if func.name() == args.func:
            function = func()
            break

    # Run the algorithm on the function
    print("Running {} and optimizing {}...".format(
          algorithm.pretty_name(), function.pretty_name()))
    rezultat = algorithm(function)
    print("Output: {!r}".format(rezultat))
