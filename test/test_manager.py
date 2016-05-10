#!/usr/bin/python

from manager import Sprint

def test_manager_get_date():
    mgr = Sprint()
    sprint_62_start_date, sprint_62_end_date = mgr.get_date(62)
    sprint_62_start_date_val = sprint_62_start_date.isoformat()
    assert sprint_62_start_date_val == '2016-05-07'
    sprint_62_end_date_val = sprint_62_end_date.isoformat()
    assert sprint_62_end_date_val == '2016-05-20'
