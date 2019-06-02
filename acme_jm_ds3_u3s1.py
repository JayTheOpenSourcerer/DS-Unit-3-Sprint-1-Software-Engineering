#!/usr/bin/env python
"""
Python module for Acme Products organization.
"""
'''Jason Meil'''
import numpy as np

class Product:
    """Example class to model an Acme Product
    """

    def __init__(self, name=None, price=10, weight=20, flammability=0.5, identifier=np.random.randint(1000000, high=10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability= flammability
        self.identifier= identifier

    def stealability(self):
        """Determines how easily stolen product is given price over weight."""
        if (self.price / self.weight) < 0.5:
            print("Not so stealable...")
        elif (self.price / self.weight) < 1:
            print("Kinda stealable.")
        else:
            print("Very stealable!")

    def explode(self):
        """Determines how explodable product is given flammability times weight."""
        if (self.flammability * self.weight) < 10:
            print("...fizzle.")
        elif (self.flammability * self.weight) < 50:
            print("...boom!")
        else:
            print("...BABOOM!!")


class BoxingGlove(Product):
    """Class to represent a boxing glove."""

    def __init__(self, name=None, price=10, weight=10, flammability=0.5, identifier=np.random.randint(1000000, high=10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier=identifier

    def explode(self):
        """If boxing glove override explode statement."""
        print("...it's a glove.")
    
    def punch(self):
        """Determines punch effect given glove weight."""
        if self.weight < 5:
            print("That tickles.")
        elif self.weight < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")