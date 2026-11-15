#!/usr/bin/env python3
"""Combine swimming and flying abilities using mixins."""


class SwimMixin:
    """Provide the ability to swim."""

    def swim(self):
        """Print the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Provide the ability to fly."""

    def fly(self):
        """Print the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim, fly, and roar."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
