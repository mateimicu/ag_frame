#!/usr/bin/env python
"""
Useful functions and constatns for all the runners.
"""


def format_output(output_args):
    """Format output for a csv format."""
    return ", ".join([str(item) for item in output_args])
