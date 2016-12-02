#!/usr/bin/env python
"""
Runner that let's you run a specific algorithm with a specific function.
"""

from __future__ import print_function

from ag_frame.runners import base
from ag_frame.runners import utils


class RunAlgorithm(base.BaseRunner):
    """Basic Runner.

    This runner let's you run and algorithm with a specific function.
    """

    NAME = "run_alg"

    def __init__(self, base_parser, subparsers, algorithms, functions):
        """Init this runner with the algorithms and function.

        :param base_parser: The base parser
        :param algorithms: A list with avalible algorithms
        :param functions: A list with avalible functions
        """
        super(RunAlgorithm, self).__init__(base_parser,
                                           subparsers,
                                           algorithms,
                                           functions)
        self._name = "run_alg"

    def _get_name(self):
        """Get the name of this runner."""
        return self.NAME

    def _add_subparser(self):
        """Add the subparser for this runner."""
        self._parser = self._subparsers.add_parser(
            self._name,
            help="Run and algorithm on a specific function.",)
        subparsers = self._parser.add_subparsers(dest="alg")
        return subparsers

    def evaluate(self):
        """Evaluate the arguments and run something if needed."""
        args = self._base_parser.parse_args()
        for item in self._algorithms + self._functions:
            item.set_args(args)

        # choose algorithm and function
        algorithm = None
        function = None
        for alg in self._algorithms:
            if alg.name() == args.alg:
                algorithm = alg()
                break
        for func in self._functions:
            if func.name() == args.func:
                function = func()
                break
        rezultat = algorithm(function)
        print(utils.format_output(rezultat))
