#!/usr/bin/python

"""Sprint Date Manager
A program to manage sprint date

Copyright (c) 2015 Copyright Shao Tian-Chen (Austin) All Rights Reserved.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from datetime import date
from itertools import count
from itertools import islice
import datetime
import logging
import re
import sys

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
        if sprint_num < 0:
            sprint_num = 0
        default_case = (0, self.GENESIS_DAY, self.GENESIS_DAY + datetime.timedelta(days=self.SPRINT_LEN.days-1))
        i, start_date, end_date = next(islice(self.get_sprints(), sprint_num, None), default_case)
        return (i, start_date, end_date)

    def get_sprints(self):
        """Given genesis dayx, sprint len l, function f, when f(x, l), output lazy evalutaion of all sprints"""
        return ((i,
            self.GENESIS_DAY + datetime.timedelta(days=self.SPRINT_LEN.days*i),
            self.GENESIS_DAY + datetime.timedelta(days=self.SPRINT_LEN.days*(i+1)-1)
        ) for i in count())

    def get_sprint(self, any_date):
        if (any_date - self.GENESIS_DAY).days < 0:
            any_date = self.GENESIS_DAY
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        s = Sprint()
        a, b, c  = s.get_sprint(date.today())
        print((a, str(b), str(c)))
    elif len(sys.argv) == 2:
        s = Sprint()
        x = sys.argv[1]
        pattern = r'^(\d+)-(\d{2})-(\d{2})$'
        if re.match(r'^[-]?\d+$', x):
            a, b, c = s.get_date(int(x))
            print((a, str(b), str(c)))
        elif re.match(pattern, x):
            yyyy, mm, dd = re.findall(pattern, x)[0]
            try:
                x_date = date(int(yyyy), int(mm), int(dd))
                a, b, c = s.get_sprint(x_date)
                print((a, str(b), str(c)))
            except:
                print('''See, you lost a date ... ''')
        else:
            print('''Hey, you need to know how to count or date ;) ''')
    else:
        print('''Hey, you need to know how to count or date ;) ''')
