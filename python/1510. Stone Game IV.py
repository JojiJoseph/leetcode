class Solution:
    @lru_cache(200000)
    def winnerSquareGame(self, n: int) -> bool:
        if int(sqrt(n))**2 == n:
            return True
        lim = int(sqrt(n)) + 1
        win = False
        for i in range(1, lim):
            win = win or not self.winnerSquareGame(n-i*i)
            if win:
                return win
        return win
