#!/usr/bin/env python3
"""Extend the built-in list with notifications."""


class VerboseList(list):
    """Print notifications when items are added or removed."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print the number of added items."""
        original_length = len(self)
        super().extend(iterable)
        count = len(self) - original_length
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Print a notification and remove the first matching item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification and return the removed item."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
