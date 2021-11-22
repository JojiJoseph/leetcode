from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append( (i, j) )
        mins = 0
        while len(q):
            l = len(q)
            for _ in range(l):
                (i, j) = q.popleft()
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append( (i-1, j) )
                if i+1 < n and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append( (i+1, j) )
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    q.append( (i, j-1) )
                if j+1 < m and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q.append( (i, j+1) )
            if len(q):
                mins += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return mins
