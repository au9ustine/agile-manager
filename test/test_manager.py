#!/usr/bin/python

from sprint_date_manager.manager import Sprint

def test_manager_sprint_init():
    mgr = Sprint('2016-01-01', 2)
    assert mgr is not None

def test_manager_get_sprint():
    from sprint_date_manager.manager import get_sprint
    assert get_sprint('2001') == 1
