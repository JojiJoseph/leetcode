from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,0,0]
        for money in nums:
            dp.append(max(dp[-2],dp[-3])+money)
        return max(dp[-1],dp[-2])
