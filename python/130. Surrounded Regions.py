class Solution:
    def dfs(self, board, m, n, i, j):
        if board[i][j] == 'X' or board[i][j] == '-':
            return 
        if board[i][j] == 'O':
            board[i][j] = '-'
        if i+1 < m:
            self.dfs(board, m, n, i+1, j)
        if i-1 >= 0:
            self.dfs(board, m, n, i-1, j)
        if j+1 < n:
            self.dfs(board, m, n, i, j+1)
        if j-1 >= 0:
            self.dfs(board, m, n, i, j-1)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            self.dfs(board, m, n, i, 0)
            self.dfs(board, m, n, i, n-1)
            # print(visited)
        for j in range(n):
            self.dfs(board, m, n, 0,j)
            self.dfs(board, m, n, m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'
