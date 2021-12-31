class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) + 1
                    max_area = max(max_area, dp[i][j]*dp[i][j])
        return max_area
