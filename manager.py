#!/usr/bin/python

import datetime
import click

# Copyright (c) 2015 Copyright Shao Tian-Chen (Austin) All Rights Reserved.
"""Sprint Date Manager
A program to manage sprint date
"""

VERSION = (1, 0, 0)

class Sprint(object):
    """Sprint entity
    """
    def __init__(self, start_date=None, sprint_len=None):
        if start_date is None:
            self.sprint_start_date = datetime.date(2013, 12, 7)
        if sprint_len is None:
            self.sprint_len = datetime.timedelta(days=14)

    def get_date(self, sprint_num):
        start_date = self.sprint_start_date + datetime.timedelta(self.sprint_len.days * (sprint_num+1))
        end_date = start_date + datetime.timedelta(self.sprint_len.days-1)
        return (start_date, end_date)

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo('Hello, World!')

if __name__ == "__main__":
    cli()
