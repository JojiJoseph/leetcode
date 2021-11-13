class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for item in nums:
            item = item % (n+1)
            nums[item-1] += (n+1)
        out = [i+1 for i in range(n) if nums[i]//(n+1) == 2]
        return out
