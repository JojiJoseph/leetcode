# Memoization solution
# class Solution:
#     @lru_cache(200000)
#     def winnerSquareGame(self, n: int) -> bool:
#         if int(sqrt(n))**2 == n:
#             return True
#         lim = int(sqrt(n)) + 1
#         win = False
#         for i in range(1, lim):
#             win = win or not self.winnerSquareGame(n-i*i)
#             if win:
#                 return win
#         return win

# DP solution
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        dp[1] = True
        for i in range(2,n+1):
            lim = int(sqrt(i))+1
            for j in range(1, lim):
                if not dp[i - j*j]:
                    dp[i] = True
                    break
        return dp[n]

