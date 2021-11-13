class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val=0
        running_sum = 0
        for item in nums:
            running_sum += item
            if running_sum < 0:
                min_val = max(min_val, -running_sum)
        return min_val+1
 