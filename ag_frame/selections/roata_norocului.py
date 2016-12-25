#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Roata norocului.
"""
from ag_frame.selections import base

import random


class Wheel(base.BaseSelection):
    """The fittest ones have the higher chance."""

    _name = "Wheel"

    def __init__(self, function, representaion):
        """Initialize an Selection algorithm.

        :param function: The function we use for selecting them.
        :param representaion: What representation is used.
        """
        super(Wheel, self).__init__(function, representaion)

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    def select(self, population):
        """Select a cromozom and return the population."""
        fit_per_item = [self._function(self._representation.decode(item)) for
                        item in population]
        total_fit = sum(fit_per_item)

        probability_per_item = [float(total_fit) / item_fit for
                                item_fit in fit_per_item]

        item_chances = [0]
        for index, item in enumerate(population):
            item_chances.append(item_chances[-1] + probability_per_item[index])

        random_item = random.random()
        item = None
        # select the item j with
        # item_chances[j] < random_item <= item_chances[j+1]
        for index in range(len(item_chances)-2):
            if item_chances[index] < random_item <= item_chances[index+1]:
                item = population[item-1]

        return item, population.remove(item)
