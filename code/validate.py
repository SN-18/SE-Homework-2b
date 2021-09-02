import functools
import json
import csv

"""
This code was created for our SE - CSC 510 class. The goal of the following code was to achieve the following:
> Can help us explore testing and setup Travis
> Can have some non-trivial requirements - for requirements.txt
> Includes some data, so that we learn to manage it securely and can better understand the 3 tenants - right to privacy, right to refuse, and right to be forgotten
> Small enough to focus on the important aspects of the homework
"""

class Calculator():
    """A basic calculator which primarily performs list based calculations
    """
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
    def list_subtract(self, values, first_sort=False):
        """Subtracts all the elements in the list and returns the result
        Args:
            values: list of elements
            first_sort: If user wants to first sort the list in descending order before the subtraction (default: False)
        Returns:
            Integer containing the total
        """
        if first_sort == False:
            return functools.reduce(lambda x, y: x-y, values)
        elif first_sort == True:
            return functools.reduce(lambda x, y: x-y, sorted(values, reverse=True))
        else:
            return None
    def list_multiply(self, values):
        """Multiplies all the elements in the list and returns the result
        Args:
            values: list of elements
        Returns:
            Integer containing the total
        """
        return functools.reduce(lambda x, y: x*y, values)
    def transform_list_add(self, values, func):
        """Uses the user defined function to transform the list and then add all the elements in the list and returns the result
        Args:
            values: list of elements
            func: User defined function used for the transformation part
        Returns:
            Integer containing the total
        """
        values = func(values)
        return functools.reduce(lambda x, y: x+y, values)
    def list_maximum(self, values):
        """Finds the maximum of all the elements in the list and returns the result
        Args:
            values: list of elements
        Returns:
            Integer containing the max value
        """
        return max(values)
    def list_minimum(self, values):
        """Finds the minimum of all the elements in the list and returns the result
        Args:
            values: list of elements
        Returns:
            Integer containing the min value
        """
        return min(values)
    def get_file_and_eval(self, file, is_json=True):
        """User can input either a json or a csv file containing keys which store 
        the equation name and strings which contain the final product to be calculated.
        For example: {"a": "3+2", "b": "5-1"} will return {"a": 5, "b": 4}
        Args:
            file: Filename to be parsed
            is_json: True - if a JSON file is passed
                     False - if a CSV file is passed
                     Default - True
        Returns:
            Dictionary of the format - {eq1: output1, eq2: output2, .....}
        """
        if is_json:
            try:
                file = json.loads(file)
            except:
                return FileNotFoundError
        else:
            try:
                file = csv.reader(file, delimiter=',')
                # file = pd.read_csv(file).to_dict()
                # Converting into a JSON format for standardization
                # for eq in file: file[eq] = list(file[eq].values())[0]
            except:
                return FileNotFoundError
        for name, eq in file.items():
            try:
                file[name] = eval(eq)
            except:
                return ValueError
        return file

if __name__ == "__main__":
    file = "../data/calculations/data.csv"
    calc = Calculator()
    print(calc.get_file_and_eval(file, is_json=False))
