class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for i in range(m-1):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[n-1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(7, 3) == 28
    assert sol.uniquePaths(3, 3) == 6
    print("Passed all test cases!")