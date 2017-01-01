#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Supervisor function for oprimising an algorithm.
"""
from __future__ import print_function
import collections
import math

from ag_frame.functions import base
from ag_frame.algorithms import basic_ag 
from ag_frame.algorithms.representations import factory as repr_factory
from ag_frame.algorithms.representations.mutations import factory as mut_factory
from ag_frame.algorithms.representations.crossovers import factory as cros_factory
from ag_frame.selections import factory as sel_factory
from ag_frame.functions import factory as func_factory


class SupervizorFunction(base.Function):
    """Supervise function to find the best parameters."""

    _name = "Supervisor Function"

    def __init__(self, **kwargs):
        """Initialize this function."""

        functions = func_factory.functions_factory()

        self._functions = [f for f in functions if f.name() not in [self.name(), "six-hump_camel_back", "tema1function"]]

        self._selections = sel_factory.selection_factory()
        self._representations = repr_factory.representations_factory()
        self._mutations = mut_factory.mutation_factory()
        self._crossovers = cros_factory.crossover_factory()

        selection_restriction = (0, len(self._selections)-.1)
        representations_restriction = (0, len(self._representations)-.1)
        mutations_restriction = (0, len(self._mutations)-.1)
        crossovers_restriction = (0, len(self._crossovers)-.1)

        population = (10, 500)
        selection_crossover = (0, 1)
        selection_mutation = (0, 1)
        generations = (1, 2000)
        precision = (2, 10)
        max_retry = (2, 50)

        self._domain_restrictions = [
            selection_restriction,
            representations_restriction,
            mutations_restriction,
            crossovers_restriction,
            population,
            selection_crossover,
            selection_mutation,
            generations,
            precision,
            max_retry,
        ]
        local_mins = (tuple([item[0] for item in self._domain_restrictions]), )

        # NOTE(mmicu): find a way to exclude the dimensions
        super(SupervizorFunction, self).__init__(
            nr_args=len(self._domain_restrictions), default_domain=(0, 0),
            local_mins=local_mins,
            )

    def prepare_domain_restrictions(self):
        """Add specific domain restrictions."""
        for index, restriction in enumerate(self._domain_restrictions):
            self.add_specific_domain_restriction(index+1, restriction)

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    @classmethod
    def add_parser(cls, base_parser):
        """Add the default parser for this function.

        :param parser: The top-level parser
        """
        super(SupervizorFunction, cls).add_parser(base_parser)
        # TODO(mmicu): add parser for:
        # - function max pop size
        # - function max_retry
        # - function max generations
        # - function max precision
        # - functions max dimensions

        cls.parser.set_defaults(dimensions=10)

    def _get_total_fitness(self, populations, function):
        """Total fitness for a population."""
        total_fit = []
        for population in populations:
            total_fit.append(sum([function.fit(*arg) for arg in population]))

        return total_fit

    def _get_fitness_increes(self, fit_list, func):
        """Fitness increes for a population."""
        inc = 0
        for index in range(1, len(fit_list)-1):
            inc += fit_list[index] - fit_list[index-1]

        return inc

    def _get_best(self, populations, func):
        """The best item from the population."""
        best = None
        for population in populations:
            for item in population:
                if not best:
                    best = item
                elif func.fit(*item) > func.fit(*best):
                    best = item
        return best

    def _clean_populations(self, pops):
        """Clean the populations."""
        populations = []
        for _, data in pops.items():
            populations.append(data)

        return populations

    def _get_fit_pop(self, populations, run_f, local_mins):
        """Return the fitness for a population."""
        pops = self._clean_populations(populations)
        fitness_per_pop = self._get_total_fitness(pops, run_f)

        total_fit = sum(fitness_per_pop)

        fit_ratio = self._get_fitness_increes(fitness_per_pop, run_f)
        best_pop = self._get_best(pops, run_f)

        good_value = abs(run_f.fit(*local_mins[0]) - run_f.fit(*best_pop))

        return total_fit * .15 + fit_ratio * .15 + good_value * .7

    def _get_value(self, info):
        """Return the fitnse from this info."""

        for function, data in info.items():
            for dimension, run_data in data.items():
                rezultat, local_mins, populations, fabicrated_args = run_data

                # prepare function
                function.set_args(fabicrated_args)
                run_f = function(dimensions=dimension)

                # get the best run
                best_run = None
                for run_id, value in populations.items():
                    if not best_run:
                        best_run = value
                    elif (self._get_fit_pop(value, run_f, local_mins) <
                          self._get_fit_pop(best_run, run_f, local_mins)):
                        best_run = value

                # compute for the best run

        return 12 

    def execute(self, *f_args):
        """This method return the value of this function for the given args.

        :param *args:
            The arguments of the function.
        """
        selection = self._selections[int(math.floor(f_args[0]))].name()
        representation = self._representations[int(
            math.floor(f_args[1]))].name()
        mutation = self._mutations[int(math.floor(f_args[2]))].name()
        crossover = self._crossovers[int(math.floor(f_args[3]))].name()

        population = int(round(f_args[4]))
        selection_crossover = f_args[5]
        selection_mutation = f_args[6]
        generations = int(math.floor(f_args[7]))
        precision = int(round(f_args[8]))
        max_retry = int(round(f_args[9]))

        values = {}
        args = collections.namedtuple(
            "args",
            ["precision", "threads", "dimensions",
             "selection", "representation", "crossover", "mutation",
             "population", "selection_mutation", "selection_crossover",
             "generations", "max_retry"])

        for function_cls in self._functions:
            values[function_cls] = {}
            for dimension in range(1, 2):
                # prepare new alg
                alg = basic_ag.BaseAG(
                    selection=selection,
                    representation=representation,
                    mutation=mutation,
                    crossover=crossover,
                    population=population,
                    selection_crossover=selection_crossover,
                    selection_mutation=selection_mutation,
                    generations=generations,
                    dimension=dimension,
                    precision=precision)

                fabicrated_args = args(
                    precision=precision, max_retry=max_retry,
                    dimensions=dimension, threads=5,
                    selection=selection,
                    representation=representation,
                    mutation=mutation,
                    crossover=crossover,
                    population=population,
                    selection_crossover=selection_crossover,
                    selection_mutation=selection_mutation,
                    generations=generations)
                alg.set_args(fabicrated_args)

                function_cls.set_args(fabicrated_args)
                function = function_cls(dimension=dimension)

                rez = alg(function)
                info = alg.get_info()

                values[function_cls][dimension] = (
                    rez, function.local_mins, info, fabicrated_args)

        return self._get_value(values)
