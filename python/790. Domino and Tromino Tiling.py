class Solution:
    @cache
    def numTilings(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        s = self.numTilings(n-1) + 2 * self.numTilings(n-2) + self.numTilings(n-3) + self.numTilings(n-4)
        
        return s % int(10**9+7)