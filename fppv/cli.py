#!/usr/bin/env python
"""cli module."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import click
import traceback

from . import version

@click.group()
@click.option('--debug', default=False, help='')
@click.version_option(version.__version__, '--version')
def cli():
    click.secho("TODO : command line tool")

if __name__ == '__main__':
    cli()


