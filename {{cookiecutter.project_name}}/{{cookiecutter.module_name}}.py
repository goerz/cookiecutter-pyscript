#!/usr/bin/env python
"""{{ cookiecutter.description }}"""
import sys
import click
from click import echo
import logging

__version__ = '{{ cookiecutter.version }}'
__author__ = '{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>'


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


if __name__ == "__main__":
    sys.exit(main())
