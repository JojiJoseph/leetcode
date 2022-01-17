class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        @lru_cache(20000)
        def calc(i, j):
            next_midx = i + n-1-j
            if next_midx >= m:
                return 0
            else:
                return max(multipliers[next_midx]*nums[i] + calc(i+1, j), multipliers[next_midx]*nums[j] + calc(i,j-1))
        return calc(0, n-1)
