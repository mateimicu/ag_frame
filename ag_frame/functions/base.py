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

    def __init__(self, name, nr_args, default_domain):
        """Initialize a function.

        Here we initialize a function with the proper informations.

        :param name:
            The name of the function
        :type name: str
        :param nr_args:
            Number of argumensts.
        :type nr_args: int
        :param default_domain:
            The default domain for every argument.
        :type default_domain: tuple
            Should be a tuple with this format (min, max).
        """
        self._name = name
        self._nr_args = nr_args
        self._default_domain = default_domain
        self._args_domain = [default_domain for _ in range(self._nr_args)]

        # Add specific domain restriction
        self.prepare_domain_restrictions()

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        raise exceptions.FunctionNotImplemented("Not Implemented.")

    @property
    def name(self):
        """Return the name of the function in a standard format."""
        return self._name.replace(" ", "_").lower()

    @property
    def pretty_name(self):
        """Return the name of the function in a pretty format."""
        return self._name

    @property
    def nr_args(self):
        """Return the number of argument of the function."""
        return self._nr_args

    @property
    def get_domain_restrictions(self):
        """Return a list with all the domain restrictions."""
        return self._args_domain

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
        for index, val in enumerate(args):
            if not (self._args_domain[index][0] <= val
                    <= self._args_domain[index][1]):
                raise function_exceptions.FunctionValueError(
                    function_name=self._name, arg_poz=index+1,
                    domain=self._args_domain[index])

        return self.execute(*args)

    def add_specific_domain_restriction(self, arg, arg_domain):
        """Add a specific domain restriction for a specific arg.

        :param arg:
            The number of the argument starting from 1.
        :type arg: int
        :param arg_domain:
            The default domain for every argument.
        :type arg_domain: tuple
            Should be a tuple with this format (min, max).
        """
        self._args_domain[arg-1] = arg_domain

    @abc.abstractmethod
    def execute(self, *args):
        """This method return the value of this function for the given args.

        :param *args:
            The arguments of the function.
        """
        pass

    def prepare_domain_restrictions(self):
        """This method add the specific domain restriction.

        This method should be overwirten if we have specific domain
        restrictions for any argument. By default it does nothing.
        """
        pass
