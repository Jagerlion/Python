"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Bryan Ruiz
Date: 12/19/2023


Build test cases for the following

before_space
after_space
first_inside_quotes
get_src
get_dst
has_error
service_response
iscurrency
exchange
"""

import introcs
import currency
import exchange


def test_before_space():
    """
    Test procedure for before_space
    """
    result = currency.before_space('Hello World')
    introcs.assert_equals('Hello', result)

    result = currency.before_space(' Hello')
    introcs.assert_equals('', result)

    result = currency.before_space('Hello ')
    introcs.assert_equals('Hello', result)

    result = currency.before_space('Hello World ')
    introcs.assert_equals('Hello', result)

    result = currency.before_space('Hello  Wor  ld ')
    introcs.assert_equals('Hello', result)

    print("Testing before_space")


def test_after_space():
    """
    Test procedure for after_space
    """

    result = currency.after_space('Hello World')
    introcs.assert_equals('World',result)

    result = currency.after_space(' Hello')
    introcs.assert_equals('Hello',result)

    result = currency.after_space('Hello ')
    introcs.assert_equals('',result)

    result = currency.after_space('Hello World ')
    introcs.assert_equals('World ',result)

    result = currency.after_space('Hello  Wor  ld ')
    introcs.assert_equals(' Wor  ld ',result)

    print("Testing after_space")


def test_first_inside_quotes():
    """
    Test procedure for first_inside_quotes
    """

    result = currency.after_space('Hello World')
    introcs.assert_equals('World',result)

    print("Testing first_inside_quotes")


def test_get_src():
    """
    Test procedure for get_src
    """
    print("Testing get_src")


def test_get_dst():
    """
    Test procedure for get_dst
    """
    print("Testing get_dst")


def test_has_error():
    """
    Test procedure for has_error
    """
    print("Testing has_error")


def test_service_response():
    """
    Test procedure for service_response
    """
    print("Testing service_response")


def test_iscurrency():
    """
    Test procedure for iscurrency
    """
    print("Testing iscurrency")


def test_exchange():
    """
    Test procedure for exchange
    """
    print("Testing exchange")


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully')
