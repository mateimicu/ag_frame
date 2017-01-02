#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Roata norocului.
"""
from ag_frame.selections import base

import random


class Turneru(base.BaseSelection):
    """The fittest ones have the higher chance."""

    _name = "Turneu"

    def __init__(self, representaion):
        """Initialize an Selection algorithm.

        :param representaion: What representation is used.
        """
        super(Wheel, self).__init__(representaion)

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    def select(self, population):
        """Select a cromozom and return the population."""
        fit_per_item = [self._function(*self._representation.decode(item)) for
                        item in population]
        pop_and_fit = zip(population, fit_per_item)
        pop_and_fit.sort(key=lambda x:x[1])

        best = pop_and_fit.pop()[0]

        population.remove(best)
        return best, population
