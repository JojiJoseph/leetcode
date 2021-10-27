class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # The idea is to move all reds to left side and all blues to right side
        # Ref: https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
        red_pointer, white_pointer, blue_pointer = 0, 0, len(nums)-1
        
        while white_pointer <= blue_pointer:
            if nums[white_pointer] == 0:
                nums[white_pointer], nums[red_pointer] = nums[red_pointer], nums[white_pointer]
                white_pointer += 1
                red_pointer += 1
            elif nums[white_pointer] == 1:
                white_pointer += 1
            else:
                nums[white_pointer], nums[blue_pointer] = nums[blue_pointer], nums[white_pointer]
                blue_pointer -= 1
