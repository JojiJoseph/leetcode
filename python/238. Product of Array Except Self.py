from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        n = len(nums)
        for i in range(n-1):
            prefix.append(nums[i]*prefix[-1])
            suffix.append(nums[n-1-i]*suffix[-1])
        suffix.reverse()
        output = [p*s for p,s in zip(prefix, suffix)]
        return output
