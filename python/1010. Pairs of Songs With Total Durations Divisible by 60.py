class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        count = [0] * 60
        for t in time:
            ans += count[-t%60]
            count[t%60] += 1
        return ans
