#!/usr/bin/python3
"""Module defining a function makeChange"""

def makeChange(coins, total):
    """
    Determing fewest number of coins needed to meet a given amount total
    Args:
        coins (list of ints): list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or
        -1 if total cannot be met by any number of coins
        0 if total <= 0
    """
    count = 0

    if total <= 0:
        return (0)
    if coins == [] or coins is None:
        return (-1)

    coins.sort(reverse=True)

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    if total > 0:
        return (-1)
    return (count)
