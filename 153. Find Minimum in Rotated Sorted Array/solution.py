class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_val = math.inf
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                min_val = min(nums[mid], min_val)
                right = mid-1
            else:
                left = mid+1
        return min(min_val, nums[right])
