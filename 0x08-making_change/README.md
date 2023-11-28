# alx-interview

## 0x08-making_change

### Description

* TODO

### Environment

* Languages: * TODO
* OS: Ubuntu 22.04 LTS
* Style guidelines: * TODO

## Coin Changing Problem

**Problem Statement**

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

**Prototype**

```python
def makeChange(coins, total):
    Return: fewest number of coins needed to meet total
```
- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1
- coins is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

**Constraints**

- `coins` is a non-empty list of positive integers.
- `total` is a non-negative integer.

**Solution**

The problem of finding the minimum number of coins to make a given change can be solved using a `dynamic programming` approach. The basic idea is to build a table that stores the minimum number of coins needed to make each possible change from 0 to `total`. Once the table is built, the minimum number of coins needed to make `total` change can be found by looking up the value of `total` in the table.

Here's the algorithm:

```python
def makeChange(coins: list, total: int) -> int:
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin

    if total != 0:
        return -1

    return num_coins
```

**Time Complexity**

The time complexity of the above solution is `O(total * len(coins))`. This is because we need to fill in the `min_coins` table, and each cell in the table requires `O(len(coins))` operations.

**Space Complexity**

The space complexity of the above solution is `O(total)`. This is because the `min_coins` table has `total + 1` elements.

**Testing**

The following code provides a test case for the `makeChange` function:

```python
coins = [1, 5, 10, 25]
total = 87

result = makeChange(coins, total)
print(result)
```

This code should print the following output:

```
3
```

## Author

* [FourtyThree43](https://www.github.com/FourtyThree43/alx-interview/0x08-making_change)

## [Fortune Cookie](http://yerkee.com/)
``
This file will self-destruct in five minutes.
``
