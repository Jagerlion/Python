"""
A module with a function to read text

This module shows off a more complicated type of precondition

Author: Bryan Ruiz
Date: 11/26/2024
"""

import introcs

def get_number(filename):
    """
    Returns the number stored in the file <filename>

    When we read a file, we get a string. This function changes the result to an int before returning the value.

    :param filename: The file to get the number from
    Precondition: filename is a string and a reference to a valid file.
    In addition, this file only ha sa single integer in it.
    """

    contents = introcs.read_txt(filename)

    # Change string to int before returning
    result = int(contents)
    return result