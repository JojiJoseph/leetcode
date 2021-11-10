class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_val = prices[0]
        for price in prices:
            if price < min_val:
                min_val = price
            else:
                if price - min_val > max_profit:
                    max_profit = price - min_val
        return max_profit
 