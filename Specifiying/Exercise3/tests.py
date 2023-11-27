"""
A test script to test the module func.py

Author: Bryan Ruiz
Date: 11/26/2023
"""
import introcs  # For assert_equals and assert_true
import funcs  # This is what we are testing


def test_replace_first():
    """
    Test procedure for replace_first
    """
    print('Testing replace_first')

    # Put your tests below this line
    result = funcs.replace_first('crane','a','o')
    introcs.assert_equals('crone',result)

    result = funcs.replace_first('poll','l','o')
    introcs.assert_equals('pool',result)

    result = funcs.replace_first('crane','cr','b')
    introcs.assert_equals('bane',result)

    result = funcs.replace_first('friday','ri','ri')
    introcs.assert_equals('friday',result)

    result = funcs.replace_first('galaxy','y','ies')
    introcs.assert_equals('galaxies',result)

# Script Code
# Do not write below this line
test_replace_first()
print('Module funcs is working correctly')
