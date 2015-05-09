#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK14 synthesizing task 02 - using a list comprehension."""


import task_01


def fibo(count):
    """Fibo sequence generation function.

    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: A list comprehension to return the numbers in a list.

    Example:
        >>> fibo(5)
        [0, 1, 1, 2, 3]

    """
    return [num for num in task_01.xfibo(count)]
