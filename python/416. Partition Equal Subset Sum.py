from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s//2
        possible_sums = set()
        for num in nums:
            temp = set()
            temp.add(num)
            for val in possible_sums:
                temp.add(val)
                if val+num <= target:
                    temp.add(val+num)
                if val == target or val+num == target:
                    return True
            possible_sums = temp
        return target in possible_sums
