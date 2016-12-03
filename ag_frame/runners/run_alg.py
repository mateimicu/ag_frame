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
        self._name = self._get_name()

    def _get_name(self):
        """Get the name of this runner."""
        return self.NAME

    @classmethod
    def is_implemented(cls):
        """If this class is implemented."""
        return True

    def _add_subparser(self):
        """Add the subparser for this runner."""
        self._parser = self._subparsers.add_parser(
            self._name,
            help="Run and algorithm on a specific function.",)
        self._parser.add_argument(
            "-o", "--output", type=str,
            help="Where to save the output(default: print it).")
        self._parser.add_argument(
            "-f", "--format", choices=utils.CHOICES,
            help="Format of the output, csv, json, xml.\n"
            "! Only csv supported for now !")
        self._parser.set_defaults(format=utils.CSV)
        subparsers = self._parser.add_subparsers(dest="alg")
        return subparsers

    def save(self, rezultat):
        """Save the output of the run."""
        format_rezult = utils.format_output(rezultat, self._args.format)

        if not self._args.output:
            print(format_rezult)
            return

        with open(self._args.output, "w+") as output:
            output.write(format_rezult)

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
