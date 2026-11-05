#!/usr/bin/python3
"""Convert CSV records to a JSON file."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Write CSV records to data.json and report whether it succeeded."""
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as file:
            records = list(csv.DictReader(file))

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

        return True
    except (OSError, csv.Error, UnicodeError, TypeError, ValueError):
        return False
