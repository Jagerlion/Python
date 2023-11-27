"""
A module with a single, non-working function.

The function in this module has a bug (in the sense that it does not satisfy its specification). This allows us to show
off testing.

Author: Bryan Ruiz
Date: 11/26/2023
"""

import introcs


def last_name_first(n):
    """
    We assume that n is just two names (first and last). Middle names are not supported.

    Examples:
        last_name_first('Walker White') returns 'White, Walker'
        last_name_first('Walker    White') returns 'White, Walker

    Precondition: n is in the form 'first-name last-name' with one or more spaces between the two names. There are no
    spaces in either <first-name> or <last-name>
    :param n: the person's name
    :return: copy of n but in the form 'last-name', first-name'
    """

    # print(n)
    end_first = introcs.find_str(n,' ')
    # print(end_first)

    first = n[:end_first]
    last = introcs.strip(n[end_first + 1:])

    return last + ', ' + first