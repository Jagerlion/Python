"""
A module to demonstrate global variables.

Author: Bryan Ruiz
Date: 11/24/2023
"""

# The global variable
VAR = 1

def next():
    """
    Returns and increments the value of VAR.
    """

    # bring in global variable VAR
    global VAR
    result = VAR

    VAR = VAR + 1

    return result