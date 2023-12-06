"""
The functions for the course project.

Author: Bryan Ruiz
Date: 12/05/2023
"""

import introcs

def matching_parens(s):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair of parentheses is an open parens '(' followed by a closing
    parens ')'.  Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    assert type(s) == str, 'The value '+repr(s)+' is not a string.'

    # Search for the first open parens '('
    first = introcs.find_str(s,'(')
    # Search for the first close parens ')' AFTER the open parens
    second = introcs.find_str(s[first:],')')
    # Compare both searches to -1 and return True if BOTH are not -1
    check1 = first == -1
    check2 = second == -1

    return not check1 and not check2


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """

    assert type(s) == str, 'The value '+repr(s)+' is not a string.'
    assert matching_parens(s), 'The string '+repr(s)+' is missing a pair of parens ()'


    # Search for the first open parens '('
    first = introcs.find_str(s,'(')
    # Search for the first close parens ')' AFTER the open parens
    second = introcs.find_str(s[first:],')')
    result = s[first+1:second+first]

    return result

