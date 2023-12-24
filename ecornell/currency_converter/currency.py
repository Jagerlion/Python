"""
Initial module for currency exchange.

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Bryan Ruiz
Date: 12/11/2023
"""

# passkey 3QQ4lj7Xif2fXphELw8AERBvzN1jJi3gB0JAIsUPDuEe

import introcs

APIKEY = '3QQ4lj7Xif2fXphELw8AERBvzN1jJi3gB0JAIsUPDuEe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, 'The value ' + repr(s) + ' is not a string.'
    assert introcs.count_str(s, ' ') >= 1, 'The string ' + repr(s) + ' does not have at least one space.'

    first = introcs.find_str(s, ' ')
    result = s[:first]

    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, 'The value ' + repr(s) + ' is not a string.'
    assert introcs.count_str(s, ' ') >= 1, 'The string ' + repr(s) + ' does not have at least one space.'

    first = introcs.find_str(s, ' ')
    result = s[first + 1:]

    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """

    assert type(s) == str, 'The value ' + repr(s) + ' is not a string.'
    assert introcs.count_str(s, '"') >= 2, 'The string ' + repr(s) + ' does not have at least two double quotes.'

    # find first double quote position in string
    first = introcs.find_str(s, '"')
    # Search for the second qutation after the first
    second = introcs.find_str(s[first + 1:], '"')
    # combining positions
    result = s[first + 1:1 + second + first]

    return result


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str, 'The value ' + repr(json) + ' is not a string.'
    assert introcs.count_str(json, '"src"') == 1, \
        'The json string ' + repr(json) + ' does not have an src substring'

    # index the position of "src" as this will be in the json stri ng
    position = introcs.index_str(json, '"src"')
    # use first_inside_quotes after finding src position to pull substring
    substring = first_inside_quotes(json[position+5:])

    return substring

def get_dst():
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str, 'The value ' + repr(json) + ' is not a string.'
    assert introcs.count_str(json, '"dst"') == 1, \
        'The json string ' + repr(json) + ' does not have an dst substring'

    # similar to src just for dst value
    position = introcs.index_str(json, '"dst"')
    substring = first_inside_quotes(json[position+5:])

    return substring

def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    # finding substring for error
    position = introcs.index_str(json, '"error"')
    substring = first_inside_quotes(json[position+7:])
    check = substring != ''

    return check

def service_response(src,dst,amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", "dst": "<dst-amount>", "error": ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    choose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition: src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition: dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """

    assert type(src) == str, 'The src value' + repr(json) + ' is not a string.'
    assert introcs.isalpha(src) == True, 'src has non alphabetic characters'
    assert len(src) > 0, 'src must be a non empty string'

    assert type(dst) == str, 'The dst value' + repr(json) + ' is not a string.'
    assert introcs.isalpha(dst) == True, 'dst has non alphabetic characters'
    assert len(dst) > 0, 'dst must be a non empty string'



    url = ('https://ecpyfac.ecornell.com/python/currency/'
           'fixed?src='+src+'&dst='+dst+'&amt='+str(amt)+'&key=3QQ4lj7Xif2fXphELw8AERBvzN1jJi3gB0JAIsUPDuEe')
    result = introcs.urlread(url)

    return result