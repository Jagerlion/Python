"""
A module with an unimplemented function 11/28/2024 1:53PM CST

This Moudle ha sa function stub that is partially completed

Author: Bryan Ruiz
Date: 11/28/2023
"""


def middle(text):
    """
    The middle starts at the length divided by 3 (rounded down) and continues until 2/3 of the string (rounded down)

    Examples:
        middle('abc') returns 'b'
        middle('abcd') returns 'b'
        middle('abcde') returns 'bc'
        middle('abcdef') returns 'cd'

    precondition: text is a strong
    :param text: the string to slice
    :return: middle 3rd of text
    """
    size = len(text)
    # find the beginning
    start = size // 3
    # finding the end
    end = 2 * size // 3
    # start and end points of text combined
    result = text[start:end]
    return result
