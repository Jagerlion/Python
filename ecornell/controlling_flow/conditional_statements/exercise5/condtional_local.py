"""
This uses a conditional to swap variable values to return a specific variable
rather than returning either or.

Bryan Ruiz
April 22, 2024
"""

def max(x,y):
    """
    Returns the max of x, y

    Precondition: x and y are numbers
    """

    if x > y :
        # temp variable for x
        # temp = x
        x = y
        y = temp

    return y