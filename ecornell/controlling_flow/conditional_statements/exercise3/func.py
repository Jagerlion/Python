"""
A function to extract names from e-mail addresses.

Author: YOUR NAME HERE
Date: THE DATE HERE
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.

    We assume (see the precondition below) that the e-mail address is in one of
    three forms:

        last.first@megacorp.com
        last.first.middle@consultant.biz
        first.last@mompop.net

    where first, last, and middle correspond to the person's first, middle, and
    last name. Names are not empty, and contain only letters. Everything after the
    @ is guaranteed to be exactly as shown.

    The function preserves the capitalization of the e-mail address.

    Examples:
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('McDougal.Raymond.Clay@consultant.biz') returns 'Raymond'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'

    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the three address formats described above
    """
    # You must use an if-elif-else statement in this function.


    if introcs.find_str(s, '@megacorp.com') > 0:
        second = introcs.find_str(s, '@')
        first = introcs.find_str(s,'.')
        result = s[first+1:second]

    else:
        second = introcs.find_str(s, '.')
        result = s[:second]

    return result