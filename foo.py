"""
A module with two functions, one calling the other

Author: Walker M. White
Date: February 14, 2019
"""

def foo(x):

    # adds 1 to x
    y = x+1
    z = bar(y)
    return z

def bar (x):
    y = x-1
    return y

w = foo(2)
print(w)