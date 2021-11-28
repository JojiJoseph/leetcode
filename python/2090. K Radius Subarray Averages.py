from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        out = [-1]*n
        if n < 2*k+1:
            return out
        running_sum = sum(nums[0:2*k+1])
        for i in range(k,n-k):
            out[i] = running_sum//(2*k+1)
            running_sum -= nums[i-k]
            if (i+k+1) < n:
                running_sum += nums[i+k+1]
        return out
