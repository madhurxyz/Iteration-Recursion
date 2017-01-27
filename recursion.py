#!python

import unittest

# Worst Case: O(n)
# Best Case: Omega(n)
# Answer: Theta(n)
def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return factorial_iterative(n)
    # return factorial_recursive(n)

def factorial_iterative(n):
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests below
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    elif n == 0 or n == 1:
        return 1
    elif n > 1:
        factorial = 1
        for i in range(0, n):
            factorial = factorial*(n-i)
        return factorial

def factorial_recursive(n):
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)
