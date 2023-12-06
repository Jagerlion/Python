"""
A module with a single greeting procedure

This module shows off a user-defined procedure, without using a function with no return value

Author: Bryan Ruiz
Date: 11/26/2023
"""

def greet(n):
    """
    Prints a greeting to the name n

    The greeting has format 'Hello <n>!' followed by a conversation starter.

    Parameter n: The name to use in the greeting
    Precondition: n is a nonempty string
    """

    print('Hello '+n+'!')
    print('How are you?')