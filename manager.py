#!/usr/bin/python

import datetime
from itertools import count
from itertools import islice
import click
import logging

# Copyright (c) 2015 Copyright Shao Tian-Chen (Austin) All Rights Reserved.
"""Sprint Date Manager
A program to manage sprint date
"""

VERSION = (1, 0, 0)

class Sprint(object):
    """Sprint entity
    """
    def __init__(self, GENESIS_DAY=None, SPRINT_LEN=None):
        """Initialized by GENESIS_DAY and SPRINT_LEN"""
        if GENESIS_DAY is None:
            self.GENESIS_DAY = datetime.date(2013, 12, 21)
        if SPRINT_LEN is None:
            self.SPRINT_LEN = datetime.timedelta(days=14)
        assert isinstance(self.GENESIS_DAY, datetime.date)
        assert isinstance(self.SPRINT_LEN, datetime.timedelta)
        assert self.SPRINT_LEN.days > 0

    def get_date(self, sprint_num):
        """Given sprint number n and function f, when f(x), then output sprint date"""
        assert isinstance(sprint_num, int)
        assert sprint_num >= 0
        default_case = (0, self.GENESIS_DAY, self.GENESIS_DAY + datetime.timedelta(days=self.SPRINT_LEN.days-1))
        i, start_date, end_date = next(islice(self.get_sprints(), sprint_num, None), default_case)
        return (start_date, end_date)

    def get_sprints(self):
        """Given genesis dayx, sprint len l, function f, when f(x, l), output lazy evalutaion of all sprints"""
        return ((i,
            self.GENESIS_DAY + datetime.timedelta(days=self.SPRINT_LEN.days*i),
            self.GENESIS_DAY + datetime.timedelta(days=self.SPRINT_LEN.days*(i+1)-1)
        ) for i in count())

    def get_sprint(self, any_date):
        for i, start_date, end_date in self.get_sprints():
            if abs((any_date - start_date).days) < self.SPRINT_LEN.days:
                return (i, start_date, end_date)

    def get_sprint_number(self, any_date):
        """Given date x and function f, when f(x), then output sprint number"""
        assert isinstance(any_date, datetime.date)
        sprint_num, start_date, end_date = self.get_sprint(any_date)
        return sprint_num

    def get_sprint_dates(self, any_date):
        """Given date x and function f, when f(x), then output sprint start date and end date"""
        assert isinstance(any_date, datetime.date)
        sprint_num, start_date, end_date = self.get_sprint(any_date)
        return (start_date, end_date)

    def get_sprint_first_day(self, any_date):
        """Given date x and function f1,f2, when f1(x), then output sprint first day"""
        start_date, _ = self.get_sprint_dates(any_date)
        return start_date

    def get_sprint_last_day(self, any_date):
        """Given date x and function f1,f2, when f2(x), then output sprint last day"""
        _, end_date = self.get_sprint_dates(any_date)
        return end_date

g_instance = None

@click.group()
@click.option("genesis-day")
@click.option("sprint-len")
def cli(genesis_day, sprint_len):
    g_instance = Sprint()

@cli.command()
@click.argument('image_name')
def hello():
    click.echo('Hello, World!')

if __name__ == "__main__":
    cli()
