#!/usr/bin/env python3
"""Print current ISO week as YYYY-Wxx."""
from datetime import date

iso = date.today().isocalendar()
print(f"{iso.year}-W{iso.week:02d}")
