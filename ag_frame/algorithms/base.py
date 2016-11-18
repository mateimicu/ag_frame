#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class for Mathematical functions.
"""
import abc

import six

from ag_frame.algorithms import utils
from ag_frame import exceptions
from ag_frame.functions import base


@six.add_metaclass(abc.ABCMeta)
class Algorithm(object):
    """Base class for every function.

    Every function should implement this methods.
    """

    def __init__(self, name):
        """Initialize an Algorithm.

        Here we initialize an Algorithm with the proper informations.

        :param name:
            The name of the Algorithm
        """
        self._name = name
        # TODO(mmicu): add more custom values for each alg

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        raise exceptions.AlgorithmsNotImplemented("Not Implemented.")

    @property
    def name(self):
        """Return the name of the function in a standard format."""
        return self._name.replace(" ", "_").lower()

    @property
    def pretty_name(self):
        """Return the name of the function in a pretty format."""
        return self._name

    def string_to_args(self, new):
        """Convert a binary string to a list of arguments.

        :param string: The binary string
        """
        return utils.string_to_args(new, self.size_var,
                                    self.domains,
                                    self.precision)

    @staticmethod
    def add_parser(base_parser):
        """Add the apropiate subparser.

        :param base_parser: The Top-Level parser.
        """
        pass

    def __call__(self, function):
        """This method will be called to run the algorithm.

        :param function:
            A `ag_frame.function.base.Function` instance.
        """
        # TODO(mmicu): implement a algorithm exception here
        if not isinstance(function, base.Function):
            raise ValueError("We don't know this function %s.", function)
        return self.execute(function)

    @abc.abstractmethod
    def execute(self, function):
        """This method will be called to run the algorithm.

        :param function:
            A `ag_frame.function.base.Function` instance.
        """
        pass
