"""
Problem 21:


121. Best Time to Buy and Sell Stock
Easy
Topics
premium lock icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    temp = prices
    while not len(temp) <= 1:
        min_i = temp.index(min(temp))

        temp_f = temp[min_i:]
        max1 = max(temp_f)

        if (max1 - temp[min_i]) > profit:
            profit = max1 - temp[min_i]
        else:
            temp = temp[:min_i]

    return  profit

        
prices = [7,1,5,3,6,4]
print(maxProfit(prices))



"""
Best sol: 

def maxProfit(prices):
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit
"""