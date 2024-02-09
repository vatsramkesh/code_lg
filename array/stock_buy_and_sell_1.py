"""You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List

def max_profit(prices: List[int]) -> int:

    min_so_far = prices[0]
    max_profit_val = 0

    for price in prices:
        min_so_far = min(min_so_far, price)
        max_profit_val = max(max_profit_val, price-min_so_far)

    return max_profit_val

if __name__ == "__main__":
    assert(max_profit([7,1,5,3,6,4])) == 5
    assert(max_profit([7,6,4,3,1])) == 0
    assert(max_profit([5, 2, 6, 1, 4])) == 4
