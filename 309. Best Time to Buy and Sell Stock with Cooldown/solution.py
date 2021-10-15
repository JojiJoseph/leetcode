class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Thanks to https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
        # Consider the following states
        # s0 - reset, s1 - buy, s2 = sell
        
        # Initial values
        s0 = 0
        s1 = -math.inf
        s2 = -math.inf
        
        for price in prices:
            s0, s1, s2 = max(s0, s2),max(s1, s0-price),s1 + price
        
        return max(s0, s2)
