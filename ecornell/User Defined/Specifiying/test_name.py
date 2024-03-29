"""
Unit test for the module name

This module demonstrates the most primitve form of testing script. It Performans the tests directly, without wrapping
them in a test procedure.

Author: Bryan Ruiz
Date: 11/26/2023
"""

# imports introcs followed by an import of name
import introcs
import name

def test_last_name_first():
    """
    Test procedure for last_name_first()
    :return:
    """
    print('Running test for last_name_first')

    result = name.last_name_first('Walker White')
    introcs.assert_equals('White, Walker', result)

    result = name.last_name_first('Walker     White')
    introcs.assert_equals('White, Walker', result)


test_last_name_first()
print('Module name is working correctly')