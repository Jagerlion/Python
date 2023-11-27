"""
A function to roll two dice. This is the second iteration for exercise 5.

Author: Bryan Ruiz
Date: 11/26/2023
"""

import random

def rollem(first=1,last=6):
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