class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)
        count = [0]*(n+1)
        for i in nums:
            count[i] += 1
        dp = [0]*(n+1)
        dp[1] = count[1]
        for i in range(2,n+1):
            dp[i] = dp[i-2] + i*count[i]
            if dp[i-1] > dp[i]:
                dp[i] = dp[i-1]
        return dp[n]
