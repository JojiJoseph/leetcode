from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        max_element, max_idx = nums[0], 0
        min_element, min_idx = nums[0], 0
        for i, item in enumerate(nums):
            if item > max_element:
                max_element, max_idx = item, i
            if item < min_element:
                min_element, min_idx = item, i
                
        # Abuse of variable names
        min_idx, max_idx = min(min_idx,max_idx), max(min_idx, max_idx)
        return min(
            min_idx+1 + (n-max_idx), # Deleting from ends
            max(min_idx, max_idx) + 1, # Deleting from left end
            max(n-min_idx, n-max_idx), # Deleting from right end
        )
