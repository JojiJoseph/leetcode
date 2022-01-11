class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = [0]*101
        ans = 0
        for item in nums:
            if item - k > 0:
                ans += count[item-k]
            if item + k < 101:
                ans += count[item+k]
            count[item] += 1
        return ans
