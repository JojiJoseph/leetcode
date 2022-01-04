class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        i = 1
        while i <= n:
            n ^= i
            i <<= 1
        return n
