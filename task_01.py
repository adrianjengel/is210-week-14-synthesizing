#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK14 synthesizing task 01 - Creating a fibonacci generator."""


def xfibo(count):
    """Fibo sequence generation function.

    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: A list of Fibonacci numbers.

    Example:
        >>> for i in xfibo(6):
        print i
        0
        1
        1
        2
        3
        5

    """
    counter = 0
    lastnum, curnum = 0, 1
    while counter < count:
        yield lastnum
        counter += 1
        lastnum, curnum = curnum, lastnum + curnum
