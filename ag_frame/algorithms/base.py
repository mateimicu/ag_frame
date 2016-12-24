#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class for Algorithms.
"""
import abc

import six

from ag_frame.algorithms import utils
from ag_frame import base_item
from ag_frame import exceptions
from ag_frame.functions import base


@six.add_metaclass(abc.ABCMeta)
class Algorithm(base_item.BaseItem):
    """Base class for every function.

    Every function should implement this methods.
    """

    _name = "Basic Algorithm"
    _parser = None
    _subparser = None

    def __init__(self):
        """Initialize an Algorithm.

        Here we initialize an Algorithm with the proper informations.
        """
        self.precision = self._args.precision
        self.max_retry = self._args.max_retry
        self.domains = None

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        raise exceptions.AlgorithmsNotImplemented("Not Implemented.")

    @classmethod
    def name(cls):
        """Return the name of the function in a standard format."""
        return cls._name.replace(" ", "_").lower()

    @classmethod
    def pretty_name(cls):
        """Return the name of the function in a pretty format."""
        return cls._name

    def string_to_args(self, new):
        """Convert a binary string to a list of arguments.

        :param string: The binary string
        """
        return utils.string_to_args(new, self.size_var,
                                    self.domains,
                                    self.precision)

    @classmethod
    def add_parser(cls, base_parser, functions_list):
        """Add the apropiate subparser.

        :param base_parser: The Top-Level parser.
        :param functions_list: the list with functions.
        """
        cls._parser = base_parser.add_parser(
            cls.name(), help="Use {}.".format(cls.pretty_name()))
        cls._subparser = cls._parser.add_subparsers(
            help="The function you want to optimize.", dest="func")
        for function in functions_list:
            function.add_parser(cls._subparser)

        cls._parser.add_argument(
            "-p", "--precision", type=int,
            help="The precision of the guesses.")
        cls._parser.add_argument(
            "-m", "--max_retry", type=int,
            help="How many times we should retry (100 default).")
        cls._parser.set_defaults(max_retry=100, precision=30)

    def _prepare_size_var(self, function):
        """Prepare the size of every var."""
        self.size_var = []

        for index in range(function.nr_args):
            size = utils.get_nr_bits(self.domains[index], self.precision)
            self.size_var.append(size)

    def __call__(self, function):
        """This method will be called to run the algorithm.

        :param function:
            A `ag_frame.function.base.Function` instance.
        """

        if not isinstance(function, base.Function):
            raise ValueError("We don't know this function %s.", function)

        global_best = None
        retry = self.max_retry
        while retry > 0:
            # Run the algorithm
            best = self.execute(function)

            if not global_best:
                global_best = best
                continue

            # Compera the global_best with the new generated best
            if function.fit(*best) > function.fit(*global_best):
                global_best = best
            retry -= 1
        return global_best

    @abc.abstractmethod
    def execute(self, function):
        """This method will be called to run the algorithm.

        :param function:
            A `ag_frame.function.base.Function` instance.
        """
        pass
