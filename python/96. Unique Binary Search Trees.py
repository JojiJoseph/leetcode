class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        soln = 0
        for i in range(n):
            soln += self.numTrees(i) * self.numTrees(n-i-1)
        return soln
