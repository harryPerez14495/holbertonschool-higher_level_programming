#!/usr/bin/env python3
"""Demonstrate multiple inheritance with fish and birds."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Describe how a fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Describe a fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Describe how a bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Describe a bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish using multiple inheritance."""

    def swim(self):
        """Describe how a flying fish swims."""
        print("The flying fish is swimming!")

    def fly(self):
        """Describe how a flying fish flies."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Describe a flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")
