from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        to_right = [0]
        to_left = [0]
        min_item = prices[0]
        for i in range(1,n):
            to_right.append(max(prices[i] - min_item, to_right[-1]))
            if prices[i] < min_item:
                min_item = prices[i]
        max_item = prices[-1]
        for i in range(n-2,-1,-1):
            to_left.append(max(max_item-prices[i], to_left[-1]))
            if prices[i] > max_item:
                max_item = prices[i]
        max_profit = 0
        for i in range(0,n):
            max_profit = max(to_right[i] + to_left[n-1-i], max_profit)
        return max_profit




6
4
0
0
11

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxProfit([3,3,5,0,0,3,1,4]) == 6
    assert solution.maxProfit([1,2,3,4,5]) == 4
    assert solution.maxProfit([7,6,4,3,1]) == 0
    assert solution.maxProfit([1]) == 0
    assert solution.maxProfit([2,1,4,5,2,9,7]) == 11
    print("Passed all test cases!")
