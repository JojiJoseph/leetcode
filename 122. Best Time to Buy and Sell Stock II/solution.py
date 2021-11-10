from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        stock = False
        profit = 0
        for i in range(n-1):
            if prices[i] <= prices[i+1] and not stock:
                profit -= prices[i]
                stock = True
            if prices[i] >= prices[i+1] and stock:
                profit += prices[i]
                stock = False
        if stock:
            profit += prices[-1]
        return profit

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7,1,5,3,6,4]) == 7
    assert sol.maxProfit([1,2,3,4,5]) == 4
    assert sol.maxProfit([7,6,4,3,1]) == 0
    assert sol.maxProfit([1]) == 0
    print("Passed all test cases!")