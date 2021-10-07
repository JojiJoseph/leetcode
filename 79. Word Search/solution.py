class Solution:
    def search(self, word, idx, board,visited, m, n, i, j):
        if idx == len(word):
            return True
        if i >=m or j >= n or i < 0 or j < 0:
            return False
        if word[idx] != board[i][j]:
            return False
        if visited[i][j]:
            return False
        visited[i][j] = True
        flag = (self.search(word, idx+1, board,visited, m, n, i+1, j) or
                self.search(word, idx+1, board,visited, m, n, i-1, j) or
                self.search(word, idx+1, board,visited, m, n, i, j+1) or
                self.search(word, idx+1, board,visited, m, n, i, j-1))
        visited[i][j] = False
        return flag

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    flag = self.search(word, 0, board,visited, m, n, i, j)
                    if flag:
                        return True
        return False
