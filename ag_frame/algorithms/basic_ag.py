#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base AG algorithm using representations and populations.
"""
import random

from ag_frame.algorithms import base
from ag_frame.algorithms.representations.crossovers import factory as cros_factory
from ag_frame.algorithms.representations import factory as repr_factory
from ag_frame.algorithms.representations.mutations import factory as mut_factory
from ag_frame.selections import factory as selection_factory
from ag_frame import utils


class BaseAG(base.Algorithm):
    """Basic algorithm."""

    _name = "base_ag"

    # If this is a combinatoric representation
    COMBINATORIC = False

    def __init__(self, **kwargs):
        """Initialize a base AG alg. This works with populations, selecitons etc.

        :param mutation: a string representing the type of mutation used
        :param representation: a string representing the type of
                               representation used
        :param crossover: a string represeting the type of crossover
        :param selection: a string  representing the type of selection
        :param population: a number representing the population number
        :param selection_crossover: The number of items to be selected for
                                    crossover
        :param selection_mutation: The number of items to be selected for
                                   mutation
        :param generations:  How many generations we should evolve
        :param dimension: The dimensions
        :param dimension: The precision
        """
        super(BaseAG, self).__init__()
        self.domains = None
        self._info = {}

        mutation_name = kwargs.get("mutation", self._args.mutation)
        representation_name = kwargs.get("representation",
                                         self._args.representation)
        crossover_name = kwargs.get("crossover", self._args.crossover)
        selection_name = kwargs.get("selection", self._args.selection)

        self._population = kwargs.get("population", self._args.population)
        self._selection_crossover = kwargs.get("selection_crossover",
                                               self._args.selection_crossover)
        self._selection_mutation = kwargs.get("selection_mutation",
                                              self._args.selection_mutation)
        self._generations = kwargs.get("generations",
                                       self._args.generations)
        dimension = kwargs.get("dimension", self._args.dimensions)
        precision = kwargs.get("precision", self._args.precision)

        crossovers = cros_factory.crossover_factory()
        mutations = mut_factory.mutation_factory()
        representations = repr_factory.representations_factory()
        selections = selection_factory.selection_factory()

        for item in crossovers:
            if crossover_name == item.name():
                self._crossover = item()
        for item in representations:
            if representation_name == item.name():
                # NOTE(mmicu): the dimension is know when we get the function
                # eliminate this requirement
                self._representation = item(dimension,
                                            precision)

        for item in mutations:
            if mutation_name == item.name():
                self._mutation = item()

        for item in selections:
            if selection_name == item.name():
                self._selection = item(self._representation)

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    @classmethod
    def add_parser(cls, base_parser, functions_list):
        """Add the apropiate subparser.

        :param base_parser: The Top-Level parser.
        :param functions_list: the list with functions.
        """
        super(BaseAG, cls).add_parser(base_parser, functions_list)
        crossovers = cros_factory.crossover_factory()
        mutations = mut_factory.mutation_factory()
        representations = repr_factory.representations_factory()
        selections = selection_factory.selection_factory()

        # add crossover
        cls._parser.add_argument("--crossover", required=True,
                                 choices=utils.get_names(crossovers),
                                 help="What crossover to use.")

        cls._parser.add_argument("--mutation", required=True,
                                 choices=utils.get_names(mutations),
                                 help="What mutation to use.")

        cls._parser.add_argument("--representation", required=True,
                                 choices=utils.get_names(representations),
                                 help="What representation to use.")

        cls._parser.add_argument("--selection", required=True,
                                 choices=utils.get_names(selections),
                                 help="What selection to use.")

        cls._parser.add_argument("--population", type=int,
                                 help="The population size.")
        cls._parser.add_argument("--selection_crossover", type=float,
                                 help="What procentage of the populations "
                                 "should be selected for crossover")
        cls._parser.add_argument("--selection_mutation", type=float,
                                 help="What procentage of the populations "
                                 "should be selected for mutation")
        cls._parser.add_argument("--generations", type=int,
                                 help="How many generations we should evolve")

        cls._parser.set_defaults(population=100, selection_crossover=0.4,
                                 selection_mutation=0.4, generations=100)

    def get_info(self):
        "Return the populations."
        return self._info

    def add_function(self, function):
        """Add the function for this run.

        :param function: Set the function
        """
        super(BaseAG, self).add_function(function)
        self._representation.add_domains_restriction(
            function.get_domain_restrictions)
        self._selection.add_function(function)

    def _split_population(self, population, selected_nr):
        """Split the population."""
        selected_genoms = []
        the_rest = population
        for _ in range(selected_nr):
            selected, the_rest = self._selection.select(the_rest)
            selected_genoms.append(selected)

        return selected_genoms, the_rest

    def _get_selected_number(self, population, rate):
        """Get the number of genoms to select."""
        return int((len(population)*rate) / 2) * 2

    def _next(self, population):
        """Return the population evolved one step."""
        # split the population for crossover
        selected, the_rest = self._split_population(
            population, self._get_selected_number(population,
                                                  self._selection_crossover))
        # crossover
        generated_items = []
        while len(selected) >= 2:
            male, female = random.sample(selected, 2)
            selected.remove(male)
            selected.remove(female)
            generated_items.extend(self._crossover.crossover(male, female))

        # if there is a impar number of selected items
        # add it back to the list
        the_rest.extend(selected)

        # Make the mutations
        selected, the_rest = self._split_population(
            the_rest, self._get_selected_number(population,
                                                self._selection_mutation))
        # crossover
        generated_items = []
        for item in selected:
            generated_items.append(self._mutation.mutate(item))

        # compute the population
        population = []
        population.extend(the_rest)
        population.extend(generated_items)

        return population

    def _add_population(self, info, index, population):
        """Add the population to the info object."""
        info[index] = [self._representation.decode(item) for
                       item in population]

    def execute(self, index):
        """The algorithm implementation."""
        info = {}
        function = self._function
        population = [self._representation.get_random() for _ in
                      range(function._nr_args)]

        # first population
        self._add_population(info, 0, population)

        for gen in range(self._generations):
            population = self._next(population)
            self._add_population(info, gen+1, population)

        # Record the population
        self._info[index] = info

        return self._representation.decode(population[0])
