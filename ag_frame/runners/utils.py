#!/usr/bin/env python
"""
Useful functions and constatns for all the runners.
"""

import os

CSV = "csv"
JSON = "json"
XML = "xml"

CHOICES = [CSV, JSON, XML]


def _format_csv(output_args):
    """Format output for a csv format."""
    return ", ".join([str(item) for item in output_args]) + os.linesep


def _format_json(output_args):
    """Format output for a json format."""
    return str(output_args)


def _format_xml(output_args):
    """Format output for a xml format."""
    return str(output_args)

FORMATERS = {
    CSV: _format_csv,
    JSON: _format_json,
    XML: _format_xml,
}


def format_output(output_args, output_format=CSV):
    """Format the output args."""
    return FORMATERS.get(output_format, CSV)(output_args)
