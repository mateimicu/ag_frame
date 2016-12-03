#!/usr/bin/env python
"""
Base Runner that handles the run of each GA.
"""

import abc

import six

from ag_frame import exceptions


@six.add_metaclass(abc.ABCMeta)
class BaseRunner(object):
    """The base runner."""

    def __init__(self, base_parser, subparsers,
                 algorithms, functions):
        """Init this runner with the algorithms and function.

        :param base_parser: The base parser
        :param subparsers: The subparsers object
        :param algorithms: A list with avalible algorithms
        :param functions: A list with avalible functions
        """
        self._name = self._get_name()
        self._base_parser = base_parser
        self._subparsers = subparsers
        self._functions = functions
        self._algorithms = algorithms
        self._parser = self._add_subparser()

        self.__add_functions_to_algorithms()

        self._args = None

    @classmethod
    def is_implemented(cls):
        """If this class is implemented."""
        raise exceptions.RunnersNotImplemented("Not Implemented.")

    def _get_name(self):
        """Get the name of this runner."""
        return self.__class__.__name__

    def __add_functions_to_algorithms(self):
        """Add the function to algorithms subparser."""
        for alg in self._algorithms:
            alg.add_parser(self._parser, self._functions)

    @abc.abstractmethod
    def _add_subparser(self):
        """Add the subparser for this runner."""
        pass

    @abc.abstractmethod
    def save(self, rezultat):
        """Save the output of the run."""
        pass

    @abc.abstractmethod
    def _evaluate(self):
        """Run the actual logic."""
        pass

    def evaluate(self):
        """Evaluate the arguments and run something if needed."""
        self._args = self._base_parser.parse_args()

        # make the arguments availible
        for item in self._algorithms + self._functions:
            item.set_args(self._args)

        # the actual evaluations
        self._evaluate()
