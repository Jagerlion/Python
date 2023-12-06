"""
This file will create initials from a name as the output

Author: Bryan Ruiz
Date: 11/28/2024
"""

import introcs


def initials(n):
    """
    Returns: The initials <first>. <last>. of the given name.

    We assume that n is just two names (first and last). Middle names are
    not supported.

    Example: initials('John Smith') returns 'J. S.'
    Example: initials('Walker White') returns 'W. W.'

    Parameter n: the person's name
    Precondition: n is in the form 'first-name last-name' with one space between names.
    There are no spaces in either <first-name> or <last-name>
    """

    # Find the first initial (and assign it to 'first')
    first = n[0] + '.'
    # Find the position of the last name (and assign it to 'pos')
    pos = introcs.find_str(n, ' ')
    # Find the last initial (and assign it to 'last')
    last = n[pos+1] + '.'
    # Compute the final answer (and assign it to 'result')
    result = first + ' ' + last
    # Return the answer
    return result