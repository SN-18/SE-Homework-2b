import pytest
import functools
import json
import pandas as pd

class Calculator():

    def __init__(self):
        pass

    def list_add(self, values):
        """Adds all the elements in the list and returns the result
        Args:
            values: list of elements
        Returns:
            Integer containing the total
        """
        return functools.reduce(lambda x, y: x+y, values)

    def list_multiply(self, values):
        """Multiplies all the elements in the list and returns the result
        Args:
            values: list of elements
        Returns:
            Integer containing the total
        """
        return functools.reduce(lambda x, y: x*y, values)

    def list_maximum(self, values):
        """Finds the maximum of all the elements in the list and returns the result
        Args:
            values: list of elements
        Returns:
            Integer containing the max value
        """
        return max(values)