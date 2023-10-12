#!/usr/bin/python3
"""
Module for minOperations
"""


def minOperations(n: int) -> int:
    """
    Returns the fewest number of operations needed to result in exactly `n` `H`
    characters in the file.
    """
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i

    return 0


def minOperations_v1(n: int) -> int:
    """
    Returns the fewest number of operations needed to result in exactly `n` `H`
    characters in the file.
    """
    if n <= 1:
        return 0

    ops = 0
    i = 2

    while i <= n:
        while n % i == 0:
            ops += i
            n //= i
        i += 1

    return ops


def minOperations_v2(n: int) -> int:
    """
    Function to calculate the minimum number of operations needed to get
    'n' 'H' characters in the file.

    The operations allowed are 'Copy All' and 'Paste'.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed.
    """
    if n <= 1:
        return 0

    ops = 0

    for i in range(2, n + 1):
        while n % i == 0:
            ops += i
            n //= i

    return ops


def minOperations_v3(n: int) -> int:
    """
    Function to calculate the minimum number of operations needed to get
    'n' 'H' characters in the file.

    The operations allowed are 'Copy All' and 'Paste'.

    Using dynamic programming to build up the solution iteratively.
    """
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')

        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)

    return dp[n]
