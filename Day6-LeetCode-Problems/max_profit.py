from typing import List

def max_profit2(prices: List[int]) -> int:
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the 
    stock at any time. However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.
    """

    profit = 0

    for i in range(1, len(prices)) : 
        if prices[i] > prices[i - 1] : 
            profit += prices[i] - prices[i - 1]
    
    return profit








def max_profit(prices: List[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in
    the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """

    n = len(prices)
    buy_day = 0
    profit = 0

    for i in range(1,n):
        if prices[i] < prices[buy_day] : 
            buy_day = i

        profit =  max(profit, prices[i] - prices[buy_day])

    return profit

def old_max_profit(prices: List[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in
    the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """

    M = 0
    n = len(prices)
    buy_prices = prices[:-1]
    if len(buy_prices) == 0 : 
        return 0
    min_buy = min(buy_prices)
    i = prices.index(min_buy)

    sell_prices = prices[i:]
    if len(sell_prices) == 0 : 
        return 0
    max_sell = max(prices[i:])
    return max(max_sell - min_buy, 0)
