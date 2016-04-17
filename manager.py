#!/usr/bin/python

# Copyright (c) 2015 Copyright Shao Tian-Chen (Austin) All Rights Reserved.
"""Sprint Date Manager
A program to manage sprint date
"""

class Sprint(object):
    """Sprint entity
    """
    def __init__(self, start_date, length):
        self.genesis_day = formulize(formulize_start_date, start_date)
        self.length = formulize(formulize_length, length)

    def __length__(self):
        return self.sprint_length()

    def next_sprint(self):
        """Get next Sprint
        """
        pass

    def prev_sprint(self):
        """Get previous Sprint
        """
        pass

    def first_day(self):
        """Get first day of this Sprint"""
        pass

    def last_day(self):
        """Get last day of this Sprint"""
        pass

    def sprint_length(self):
        """Get length of Sprint"""
        pass

def get_sprint(given_date):
    """Given any date, return the Sprint containing that date
    Given other value or current date, provide current Sprint
    """
    return 1

def formulize(formulize_fn, raw_data):
    """Formulize data or data string to align corresponding data"""
    return formulize_fn(raw_data)

def formulize_start_date(raw_date):
    """Formulize Sprint start date"""
    pass

def formulize_length(raw_length):
    """Formulized Sprint length"""
    pass

def main():
    print('Hello, World')

if __name__ == "__main__":
    main()
