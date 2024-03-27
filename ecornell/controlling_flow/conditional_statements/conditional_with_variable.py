def max(x,y):
    """
    Returns: max of x or y

    Precondition: x and y are numbers. Integer or float
    """

    if x > y:
        temp = x # changes y to x by using local variable.
        x = y
        y = temp
    # notice how return is not under the if statement
    return y