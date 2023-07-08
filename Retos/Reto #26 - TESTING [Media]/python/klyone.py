#!/usr/bin/env python3

import pytest
import calendar
import datetime

# Run tests with pytest

def is_there_13_friday(month, year, debug=False):
    cal = calendar.Calendar()

    if debug:
        print(calendar.month(year, month))

    for day in cal.itermonthdays2(year, month):
        if day[0] == 13:
            break

    if day[1] == calendar.FRIDAY:
        return True
    else:
        return False

def test_nothing():
    pass

def test_invalid_year():
    assert not is_there_13_friday(1,-1500000)

def test_invalid_year2():
    assert not is_there_13_friday(1, datetime.MINYEAR-1)

def test_invalid_year3():
    assert not is_there_13_friday(1, datetime.MAXYEAR+1)

def test_invalid_month():
    with pytest.raises(calendar.IllegalMonthError):
        is_there_13_friday(-5, 1900)

def test_no_friday_13nd():
    assert not is_there_13_friday(1, 1900)
    assert not is_there_13_friday(3, 1988)
    assert not is_there_13_friday(3, 1991)
    assert not is_there_13_friday(6, 2023)

def test_friday_13nd():
   assert is_there_13_friday(1, 2012)
   assert is_there_13_friday(4, 2012)
   assert is_there_13_friday(7, 2012)
   assert is_there_13_friday(3, 2020)
