"""
A module with an incomplete function.

This function was implemented using the backwards-design technique.

Author: Bryan Ruiz
Date: 11/28/2023
"""
import introcs


def second_in_list(s):
    """
    Returns: the second item in comma-separated list

    The final result should not have any whitespace around the edges.

    Example: second_in_list('apple, banana, orange') returns 'banana'
    Example: second_in_list('  do  ,  re  ,  me  ,  fa  ') returns 're'
    Example: second_in_list('z,y,x,w') returns 'y'

    Parameter s: The list of items
    Precondition: s is a string of at least three items separated by commas.
    """

    # add result assignement

    array = introcs.split(s, ',')[1]
    result = introcs.strip(array)
    return result
