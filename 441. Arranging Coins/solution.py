from math import sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = int(sqrt(2*n))
        if k*(k+1) > 2*n:
            return k-1
        else:
            return k
