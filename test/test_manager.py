#!/usr/bin/python

from manager import Sprint
import datetime
import logging

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

def test_manager_get_date():
    mgr = Sprint()
    sprint_62_start_date, sprint_62_end_date = mgr.get_date(62)
    sprint_62_start_date_val = sprint_62_start_date.isoformat()
    LOG.debug('sprint_62_start_date_val: %s', sprint_62_start_date_val)
    assert sprint_62_start_date_val == '2016-05-07'
    sprint_62_end_date_val = sprint_62_end_date.isoformat()
    LOG.debug('sprint_62_end_date_val: %s', sprint_62_end_date_val)
    assert sprint_62_end_date_val == '2016-05-20'

def test_manager_get_sprint_number():
    mgr = Sprint()
    today = datetime.date(2016, 5, 11)
    actual_sprint_number = mgr.get_sprint_number(today)
    LOG.debug('actual_sprint_number: %s', actual_sprint_number)
    expected_sprint_number = 62
    assert actual_sprint_number == expected_sprint_number
    today = datetime.date(2016, 5, 7)
    actual_sprint_number = mgr.get_sprint_number(today)
    LOG.debug('actual_sprint_number: %s', actual_sprint_number)
    expected_sprint_number = 62
    assert actual_sprint_number == expected_sprint_number

def test_manager_get_sprint_dates():
    mgr = Sprint()
    today = datetime.date(2016, 5, 11)
    actual_sprint_start_date, actual_sprint_end_date = mgr.get_sprint_dates(today)
    assert actual_sprint_start_date.isoformat() == '2016-05-07'
    assert actual_sprint_end_date.isoformat() == '2016-05-20'

def test_manager_get_first_or_last_day():
    mgr = Sprint()
    today = datetime.date(2016, 5, 11)
    actual_sprint_start_date = mgr.get_sprint_first_day(today)
    actual_sprint_end_date = mgr.get_sprint_last_day(today)
    assert actual_sprint_start_date.isoformat() == '2016-05-07'
    assert actual_sprint_end_date.isoformat() == '2016-05-20'
