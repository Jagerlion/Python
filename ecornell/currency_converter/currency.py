"""
Initial module for currency exchange.

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Bryan Ruiz
Date: 12/11/2023
"""

# passkey 3QQ4lj7Xif2fXphELw8AERBvzN1jJi3gB0JAIsUPDuEe

import introcs

APIKEY = '3QQ4lj7Xif2fXphELw8AERBvzN1jJi3gB0JAIsUPDuEe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, 'The value ' + repr(s) + ' is not a string.'
    assert introcs.count_str(s,' ') >= 1, 'The string '+repr(s)+' does not have at least one space.'

    first = introcs.find_str(s, ' ')
    result = s[:first]

    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, 'The value ' + repr(s) + ' is not a string.'
    assert introcs.count_str(s,' ') >= 1, 'The string '+repr(s)+' does not have at least one space.'

    first = introcs.find_str(s, ' ')
    result = s[first + 1:]

    return result

def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """

    # find first double quote position in string
    first = introcs.find_str(s,'"')
    # Search for the second qutation after the first
    second = introcs.find_str(s[first+1:],'"')
    # combining positions
    result = s[first+1:1+second+first]

    return result

