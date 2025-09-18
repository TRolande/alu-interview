#!/usr/bin/python3
"""
0-minoperations module
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    to reach exactly n H characters.

    Args:
        n (int): target number of characters

    Returns:
        int: minimum number of operations, or 0 if impossible
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

