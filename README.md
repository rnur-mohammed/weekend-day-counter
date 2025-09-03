# Weekend Day Counter

A Python CLI tool that calculates how many weekend days (Saturdays & Sundays) fall between two given dates (inclusive).

## ✨ Features
- Accepts two dates as command-line arguments in `YYYY-MM-DD` format.
- Validates input dates and handles leap years.
- Implements helper functions:
  - `leap_year()` → check leap years
  - `mon_max()` → maximum days in a month
  - `after()` → get the next day
  - `valid_date()` → validate date strings
  - `day_count()` → count weekend days between two dates

## 🚀 Usage
Run from the command line:
```bash
python3 assignment1.py 2024-01-01 2024-12-31

Example output:
The period between 2024-01-01 and 2024-12-31 includes 104 weekend days.
