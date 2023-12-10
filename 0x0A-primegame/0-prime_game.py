#!/usr/bin/python3
""" Module prime_game
"""


def isWinner(x: int, nums: list):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0:n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'


# def is_prime(n):
#   """chechk prime"""
#   return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# m = max(l)
# primes = [True for _ in range(1, m + 1, 1)]
# primes[0] = False

# print(primes)

# evens = [i for i in l if i % 2 == 0]
# odds = [i for i in l if i % 2 != 0]
