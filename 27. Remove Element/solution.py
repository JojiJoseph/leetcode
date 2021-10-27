class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums)-1
        left = 0
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                nums.pop()
                right -= 1
            else:
                left += 1
