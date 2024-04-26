"""
Functions to anglicize intgers in the range 1...999,999

The primary function of thi smodule is anglicize().

Author: Walker M White
Date: March 30, 2019
"""

def anglicize(n):
    """
    Returns: English equivalent of n.

    Examples:
        3 - "three"
        45 - "forty five"
        100 - "one hundred"
        127 - "one hundred twenty seven"
        10001 - "one thousand one"
        990099: "nine hundred ninety thousand ninety nine

    Parameter: the integer to anglicize
    Precondition: 0 < n < 1,000,000
    """

    if n < 1000:
        return anglicize1000(n)

    # n >= 1000
    # conditional expression to get number 1...999
    if n % 1000 == 0:
        suffix = ''
    else:
        suffix = ' '+anglicize1000(n % 1000)
    return (anglicize1000(n//1000) + ' thousand'+ suffix)

def anglicize1000(n):
    """
    Return anglicize of numbers between 0<n<1000
    """

    if n < 20:
        return anglicize1to19(n)
    elif n < 100:
        # n >== 20
        return anglicize20to99(n)
    else:
        # n >== 100
    return anglicize100to999(n)

# Not complete

