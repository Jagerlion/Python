"""
Conversion functions for Fahrenheit and Celsius

This module shows off two functions for converting temperature back and forth between fahrenheit and centigrade.
It also shows how to use variables to represent "constants", or values that we give a name in order to remember better.

Author: Bryan Ruiz
Date: 11/26/2023
"""

def to_centrigrade(x):
    """
    Returns: x converted to centigrade

    The value returned has type float.

    :parameter x: the temperature in Fahrenheit
    Precondition: x is a float
    """

    return 5*(x-32)/9.0


def to_fahrenheit(x):
    """
    Returns: x converted to Fahrenheit

    The value returned has type float.

    :parameter x: the temperature in centigrade
    Precondition: x is a float
    """

    return 9*(x+32)/5.0