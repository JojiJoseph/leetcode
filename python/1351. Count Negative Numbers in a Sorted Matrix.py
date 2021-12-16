class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        i,j = n-1,0
        while i >= 0 and j < m:
            if grid[i][j] >= 0:
                j += 1
            else:
                ans += (m-j)
                i -= 1
        return ans
