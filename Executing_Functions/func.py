"""
A function to roll two dice

Author: Bryan Ruiz
Date: 11/24/2023
"""

import random

def rollem(first,last):
    """
    Returns the sum of two random numbers.

    The numbers generated are between first and last (inclusive).

    Example: rollem(1,6) can return any value between 2 and 12.


    Parameter first: The lowest possible number
    Precondition: first is an integer

    Parameter last: The greatest possible number
    Precondition: last is an integer, last >= first
    """
    #print('Choosing two numbers between '+str(first)+' and '+str(last)+'.')

    # Generate two numbers, add, and print the result
    num1 = random.randint(first,last)
    num2 = random.randint(first,last)
    thesum = num1+num2
    #print('The sum is '+str(thesum)+'.')

    return thesum