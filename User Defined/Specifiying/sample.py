"""
This is a self-made sample module to see if the input is an integer
"""

import introcs

def is_integer(a):
    """
    This function will detect if the inputted variable is an integer

    :parameter: a is the input from the user
    Precondition: a must be an integer of some kind, float or not
    :return: if 2 is the input the return will be True.
    """
    print('Was the input an integer:')
    result = introcs.isint(a)

    return result