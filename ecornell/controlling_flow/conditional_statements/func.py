"""
A function to search for the first vowel position

Author: Bryan Ruiz
Date: 01/05/2024
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns len(s) if there are no vowels.

    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.

    Examples:
        first_vowel('hat') returns 1
        first_vowel('grrm') returns 4
        first_vowel('sky') returns 2
        first_vowel('year') returns 1

    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """

    result = len(s)  # In case there is no 'a'

    if 'a' in s and introcs.index_str(s, 'a') < result:
        result = introcs.index_str(s, 'a')

    if 'e' in s and introcs.index_str(s, 'e') < result:
        result = introcs.index_str(s, 'e')

    if 'i' in s and introcs.index_str(s, 'i') < result:
        result = introcs.index_str(s, 'i')

    if 'o' in s and introcs.index_str(s, 'o') < result:
        result = introcs.index_str(s, 'o')

    if 'u' in s and introcs.index_str(s, 'u') < result:
        result = introcs.index_str(s, 'u')

    if introcs.find_str(s, 'y', 1) > 0 and introcs.index_str(s, 'y') < result:
        result = introcs.index_str(s, 'y', 1)

    return result
