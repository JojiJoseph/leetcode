class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        odd_one = 0
        for num in nums:
            odd_one ^= num
        return odd_one
