#!/usr/bin/python3
"""Define an abstract animal and concrete animal subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Define the interface shared by all animals."""

    @abstractmethod
    def sound(self):
        """Define the sound an animal must provide."""
        pass


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow"
