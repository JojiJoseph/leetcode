from copy import deepcopy
from typing import List


class Solution:
    def dfs(self, grid, visited, i, j, rem):
        n = len(grid)
        m = len(grid[0])
        count = 0
        if i >= n or i < 0 or j >= m or j < 0:
            return 0
        elif visited[i][j]:
            return 0
        elif grid[i][j] == 2 and rem == 0:
            return 1
        elif grid[i][j] == -1:
            return 0
        visited[i][j] = 1
        count += self.dfs(grid, visited, i+1, j, rem-1)
        count += self.dfs(grid, visited, i-1, j, rem-1)
        count += self.dfs(grid, visited, i, j+1, rem-1)
        count += self.dfs(grid, visited, i, j-1, rem-1)
        visited[i][j] = 0
        return count

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = deepcopy(grid)
        start_pt = (0, 0)
        rem = 0
        for i in range(n):
            for j in range(m):
                visited[i][j] = 0
                if grid[i][j] == 1:
                    start_pt = (i, j)
                if grid[i][j] == 0:
                    rem += 1
        n = self.dfs(grid, visited, start_pt[0], start_pt[1], rem+1)
        return n


if __name__ == "__main__":
    soln = Solution()
    assert soln.uniquePathsIII(
        [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
    assert soln.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
    assert soln.uniquePathsIII([[0, 1], [2, 0]]) == 0
    print("Passed all test cases!")
