class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1) # Clear least significant set bit
            ans += 1
        return ans