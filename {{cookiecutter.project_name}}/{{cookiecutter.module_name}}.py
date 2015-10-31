#!/usr/bin/env python
"""{{ cookiecutter.description }}"""
# Copyright (C) {{cookiecutter.year}} {{cookiecutter.author_name}}. See LICENSE for terms of use.
import sys
import logging

import click
from click import echo

__version__ = '{{ cookiecutter.version }}'


@click.command()
@click.help_option('--help', '-h')
@click.version_option(version=__version__)
@click.option('--debug', is_flag=True,
    help='enable debug logging')
def main(debug):
    """{{ cookiecutter.description }}"""
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Enabled debug output")

