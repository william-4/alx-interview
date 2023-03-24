#!/usr/bin/python3
"""Defines a solution to the minimum operations method"""


def minOperations(n):
    """Method that solves the minimum operations puzzle    """
    op = 0
    min_op = 2
    while n > 1:
        while n % min_op == 0:
            op += min_op
            n /= min_op
        min_op += 1
    return op
