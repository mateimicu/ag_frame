#!/usr/bin/env python
"""
Base class for Mathematical functions.
"""
import abc

import six

from ag_frame import exceptions
from ag_frame.functions import exceptions as function_exceptions


@six.add_metaclass(abc.ABCMeta)
class Function(object):
    """Base class for every function.

    Every function should implement this methods.
    """

    def __init__(self, name, nr_args):
        self._name = name
        self._nr_args = nr_args

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        raise exceptions.FunctionNotImplemented("Not Implemented.")

    @property
    def name(self):
        """Return the name of the function."""
        return self._name

    @property
    def nr_args(self):
        """Return the number of argument of the function."""
        return self._nr_args

    def __call__(self, *args):
        """This method return the value of this function for the given args.

        If the number of argument is lower then the expected needed numner, an
        `ag_fram.functions.exception.ToFewArguments` exception will be raised.
        :param *args:
            The arguments of the function.
        """
        if len(args) < self._nr_args:
            raise function_exceptions.ToFewArguments(function_name=self._name,
                                                     nr_args=self._nr_args,
                                                     given_nr_args=len(args))
        return self.execute(*args)

    @abc.abstractmethod
    def execute(self, *args):
        """This method return the value of this function for the given args.

        :param *args:
            The arguments of the function.
        """
        pass
