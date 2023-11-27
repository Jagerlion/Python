"""
A test script to test the module funcs.py

Author: Bryan Ruiz
Date: 11/27/2023
"""

import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing

# Two test functions for vowels, one for y on its own.

def test_has_a_vowel():
    """
    Test procedure for has_a_vowel
    :return:
    """
    print('Testing has_y_vowel')

    result = funcs.has_a_vowel('aeiou')
    introcs.assert_equals(True,result)

    result = funcs.has_a_vowel('ham')
    introcs.assert_equals(True,result)

    result = funcs.has_a_vowel('sky')
    introcs.assert_equals(False,result)

    result = funcs.has_a_vowel('letter')
    introcs.assert_equals(True,result)

    result = funcs.has_a_vowel('winner')
    introcs.assert_equals(True,result)

    result = funcs.has_a_vowel('food')
    introcs.assert_equals(True,result)

    result = funcs.has_a_vowel('bunker')
    introcs.assert_equals(True,result)

    result = funcs.has_a_vowel('friday')
    introcs.assert_equals(True,result)

    result = funcs.has_a_vowel('aaaaa')
    introcs.assert_equals(True,result)

    result = funcs.has_a_vowel('xxxu')
    introcs.assert_equals(True,result)

def test_has_y_vowel():
    """
    Test procedure for has_y_vowel
    :return:
    """
    print('Testing has_a_vowel')

    result = funcs.has_y_vowel('friday')
    introcs.assert_equals(True,result)

# String informing user test completed successfully
test_has_a_vowel()
test_has_y_vowel()
print('Module funcs is working correctly')
