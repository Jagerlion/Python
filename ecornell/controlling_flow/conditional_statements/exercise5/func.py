"""
A function to check the validity of a numerical string

Author: Bryan Ruiz
Date: 04/25/2024
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.

    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.

    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).

    Examples:
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False

    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """

    # find the length of s string

    length = len(s)
    # print(length)

    if s[0] == '0' and length > 1:
        return False

    elif length <= 3:

        return introcs.isint(s)

    elif ',' in s and length > 3:

        result = introcs.index_str(s, ',')

        # index of comma staring from the right
        comma_pos = length - result - 1

        # Checks the last 3 characters are digits before checking characters in front of the comma
        if comma_pos == 3 and introcs.isint(s[result + 1:]):

            return introcs.isint(s[:result])

    return False