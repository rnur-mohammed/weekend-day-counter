#!/usr/bin/env python3

# Author: Nur Mohammed Rasel
# Student ID: 153510235
# OPS445 Assignment 1
#
# Academic Honesty Declaration:
# I declare that this assignment is my own work in accordance with Seneca Academic Policy.
# No part of this assignment has been copied manually or electronically from any other source.

import sys

def usage():
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")

def leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def mon_max(month: int, year: int) -> int:
    if month == 2:
        return 29 if leap_year(year) else 28
    days_in_month = {
        1: 31, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return days_in_month.get(month, 0)

def after(date: str) -> str:
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1
    if tmp_day > mon_max(month, year):
        tmp_day = 1
        tmp_month = month + 1
        if tmp_month > 12:
            tmp_month = 1
            year += 1
        month = tmp_month
    else:
        day = tmp_day

    return f"{year:04d}-{month:02d}-{tmp_day:02d}"

def valid_date(date: str) -> bool:
    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        return False
    try:
        str_year, str_month, str_day = date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
    except ValueError:
        return False

    if year < 1 or month < 1 or month > 12:
        return False

    max_day = mon_max(month, year)
    return 1 <= day <= max_day

def day_count(start: str, end: str) -> int:
    days = 0
    current = start

    while current <= end:
        year, month, day = map(int, current.split('-'))

        if month < 3:
            month += 12
            year -= 1
        q = day
        m = month
        k = year % 100
        j = year // 100

        h = (q + ((13*(m + 1)) // 5) + k + (k // 4) + (j // 4) + (5*j)) % 7
        if h == 0 or h == 1:
            days += 1

        current = after(current)

    return days

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    if not valid_date(start_date) or not valid_date(end_date):
        usage()
        sys.exit(1)

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    weekends = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")

