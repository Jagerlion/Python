"""
This file is about relearning python fundamentals for intermediate python
Author: Bryan Ruiz
Date: 01/19/2024
"""

# importing, just like it sounds, pulls a file into the code.
import hello

# float is a number with decmials, it is not a whole number in other words
number1 = 3.1452525
number2 = 5353.434
number3 = 55
number4 = 45.6

# integer is a whole number, no decimals, no fractions
number5 = 5
number6 = 23423423423
number7 = 62345.3
number8 = -23

# boolean, True, False, does need to be captilized
value1 = True
value2 = False

# strings are usually alphabetic characters (abcde...), non-numeric (#$"...)
# HOWEVER, you can still put floats and integers as strings
# strings are typically in single quotes

value3 = 'this is a string'
value4 = 'this is a string "with symbols **()'
value5 = '3434'  # strings can have numbers too
value6 = '3.44'  # strings can have floats

# print function, this outputs some kind of value. typically in a terminal.
print(value4)
print('hi im struggling help')
print('This test: ')
print('another test..' + 'were' + 'trying.')


# functions can be made within python that are not built in.
# to do this, type: def function_name(some variable):
# usually this is followed by a docstring to explain what the function is.

def power_trip():
    """
    this is a function that takes in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       1 or 2 and puts out
    a string value.

    number16 is an integer 1 or 2
    """

    # this is where the code goes
    global number1
    number1 = 4.0

    # return will , spit out whatever calculated value is for this function
    return number1


# function calling, you type the function name with the parameter
# ex: function_name(variable, parameter1, parameter2) usually up to 4
# if the function is not in the file or python, or else
# the program will not know where to pull the function.
# ex: filename.function_name(variable, parameter)


a = power_trip()
print(a)

# you MUST import the file first
hello.wallie('string')
hello.wallie(2)


potato = hello.addition(1)
print(potato)