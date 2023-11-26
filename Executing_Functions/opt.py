"""
A module to show off optional arguments

Author: Bryan Ruiz
Date: 11/26/2023
"""

def point_str(x=0,y=0,z=0):
    """
    Returns a String Repr of a point.

    Parameter x: the x coordinate
    Precondition: x is a number

    Parameter y: the y coordinate
    Precondition: y is a number

    Parameter z: the z coordinate
    Precondition: z is a number
    """

    # Convert all numbers to floats
    x = float(x)
    y = float(y)
    z = float(z)

    result = '('+str(x)+','+ str(y)+','+ str(z)+')'

    return result