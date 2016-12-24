#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Exception module for all exceptions.
"""


class AGBaseException(Exception):
    """Base exception for the AG Framework."""
    pass


class FunctionException(AGBaseException):
    """Base exception for the AG Framework Functions."""
    pass


class AlgorithmException(AGBaseException):
    """Base exception for the AG Framework Algorithms."""
    pass


class AGNotImplemented(AGBaseException):
    """Base exception for not implemented classes."""
    pass


class FunctionNotImplemented(AGNotImplemented):
    """Exceptions for not implemented functions."""
    pass


class AlgorithmsNotImplemented(AGNotImplemented):
    """Exceptions for not implemented Algorithms."""
    pass


class RunnersNotImplemented(AGNotImplemented):
    """Exceptions for not implemented Runner."""
    pass


class RepresentationNotImplemented(AGNotImplemented):
    """Exceptions for not implemented Representation."""
    pass


class MutationNotImplemented(AGNotImplemented):
    """Exceptions for not implemented Mutation."""
    pass


class CrossoverNotImplemented(AGNotImplemented):
    """Exceptions for not implemented Crossover."""
    pass


class SelectionNotImplemented(AGNotImplemented):
    """Exceptions for not implemented Selection."""
    pass
