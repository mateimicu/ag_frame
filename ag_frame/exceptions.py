#!/usr/bin/env python
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
