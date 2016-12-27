#!/usr/bin/env python
"""
Runner that let's you run a specific algorithm with a specific function.
"""

from __future__ import print_function


# pragma:pylint-disable too-long-line
from ag_frame.algorithms.representations import factory as repr_factory
from ag_frame.algorithms.representations.mutations import factory as mutation_factory
from ag_frame.algorithms.representations.crossovers import factory as crossoer_factory
from ag_frame.runners import base
from ag_frame.runners import utils
from ag_frame import utils


class RunAG(base.BaseRunner):
    """Basic Runner.

    This runner let's you run and algorithm with a specific function.
    """

    NAME = "run_ag"

    def __init__(self, subparsers, algorithms, functions):
        """Init this runner with the algorithms and function.

        :param algorithms: A list with avalible algorithms
        :param functions: A list with avalible functions
        """
        super(RunAG, self).__init__(subparsers,
                                    algorithms,
                                    functions)
        self._name = self._get_name()

        self._add_new_items()

    def _get_name(self):
        """Get the name of this runner."""
        return self.NAME

    def _filter_items(self, items):
        """Filter this items."""
        return items

    def _add_new_items(self):
        """Add new items for this runner."""
        crossovers = self._filter_items(crossoer_factory.crossover_factory())
        mutations = self._filter_items(mutation_factory.mutation_factory())
        representaions = self._filter_items(
            repr_factory.representations_factory())

        self._parser.add_argument("--crossover",
                                  help="What crossover algorithm to use.",
                                  choices=utils.get_names(crossovers))

        self._parser.add_argument("--mutation",
                                  help="What mutation algorithm to use.",
                                  choices=utils.get_names(mutations))
        self._parser.add_argument("--representation",
                                  help="What representation algorithm to use.",
                                  choices=utils.get_names(representaions))

    @classmethod
    def is_implemented(cls):
        """If this class is implemented."""
        return True

    def _evaluate(self):
        """Evaluate the arguments and run something if needed."""
        # choose algorithm and function
        algorithm = None
        function = None
        for alg in self._algorithms:
            if alg.name() == self._args.alg:
                algorithm = alg()
                break
        for func in self._functions:
            if func.name() == self._args.func:
                function = func()
                break

        rezultat = algorithm(function)
        self.save(rezultat)
