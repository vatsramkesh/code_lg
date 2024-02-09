"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the
 stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    profit = 0
    buy_price = 0
    sell_price = 0

    for i, v in enumerate(prices[1:], 1):
        if v > prices[i-1]:
            profit += v-prices[i-1]
        # if v > prices[i+1]:
        #     sell_price = v
        # else:
        #     buy_price = v 
        # if sell_price and buy_price:
        #     profit += sell_price-buy_price


    return profit



if __name__ == "__main__":
    assert(max_profit([5, 2, 6, 1, 4, 7, 3, 6])) == 13
    assert(max_profit([7,1,5,3,6,4])) == 7
    assert(max_profit([1,2,3,4,5])) == 4
    assert(max_profit([7,6,4,3,1])) == 0


