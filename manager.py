#!/usr/bin/env python3

"""Sprint Date Manager
A tiny tool to manage sprint date

Copyright (c) 2015-2019 Copyright Shao Tianchen
All Rights Reserved.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from datetime import date
from itertools import count
from itertools import islice
import datetime
import argparse

VERSION = (1, 1, 0)


class Sprint(object):
    """Sprint entity
    """

    def __init__(self, GENESIS_DAY, SPRINT_LEN):
        """Initialized by GENESIS_DAY and SPRINT_LEN"""
        self.GENESIS_DAY = GENESIS_DAY
        self.SPRINT_LEN = SPRINT_LEN
        assert isinstance(self.GENESIS_DAY, datetime.date)
        assert isinstance(self.SPRINT_LEN, datetime.timedelta)
        assert self.SPRINT_LEN.days > 0

    def get_date(self, sprint_num):
        """Given sprint number n and function f, when f(x), then output sprint date"""
        assert isinstance(sprint_num, int)
        if sprint_num < 0:
            sprint_num = 0
        default_case = (0, self.GENESIS_DAY, self.GENESIS_DAY +
                        datetime.timedelta(days=self.SPRINT_LEN.days-1))
        i, start_date, end_date = next(
            islice(self.get_sprints(), sprint_num, None), default_case)
        return (i, start_date, end_date)

    def get_sprints(self):
        """Given genesis dayx, sprint len l, function f, when f(x, l), output lazy evalutaion of all sprints"""
        return ((i,
                 self.GENESIS_DAY +
                 datetime.timedelta(days=self.SPRINT_LEN.days*i),
                 self.GENESIS_DAY +
                 datetime.timedelta(days=self.SPRINT_LEN.days*(i+1)-1)
                 ) for i in count())

    def get_sprint(self, any_date):
        if (any_date - self.GENESIS_DAY).days < 0:
            any_date = self.GENESIS_DAY
        for i, start_date, end_date in self.get_sprints():
            if abs((any_date - start_date).days) < self.SPRINT_LEN.days:
                return (i, start_date, end_date)

    def __str__(self):
        i: int
        start_date: datetime.date
        end_date: datetime.date
        i, start_date, end_date = self.get_sprint(date.today())
        return str((
            i,
            start_date.isoformat(),
            end_date.isoformat()
        ))

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--genesis-day', type=str, default='2013-12-21')
    parser.add_argument('--sprint-len', type=int, default=14)
    parser.add_argument('--version', action='version',
                        version='v' + '.'.join(map(str, VERSION)))
    args = parser.parse_args()
    genesis_day = datetime.date.fromisoformat(args.genesis_day)
    if datetime.date.today().year > 2019:
        # 2019-W26-1: Calibrate sprints to align ISO weekdays
        genesis_day += datetime.timedelta(days=2)
    sprint_len = datetime.timedelta(days=args.sprint_len)
    s = Sprint(
        genesis_day,
        sprint_len
    )
    print(str(s))


main()
