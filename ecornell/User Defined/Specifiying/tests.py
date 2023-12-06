"""
A test script to test the module funcs.py

Author: Bryan Ruiz
Date: 11/26/2023
"""

import introcs      # For assert_equals
import funcs        # This is what we are testing


# Put your code below this line, these all test the function has_a_vowel in different variations.
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

# Do not write below this line
print('Module funcs is working correctly')
