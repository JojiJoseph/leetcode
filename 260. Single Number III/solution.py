class Solution:
    def right_most_setbit(self, n):
        k = 0
        while n & (1<<k) == 0:
            k += 1
        return k
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Thanks to: https://leetcode.com/problems/single-number-iii/discuss/1561785/Java-Simple-Bit-Manipulation-using-XOR-or-Two-Pass-or-Beats-100-0ms-or-TC:O(N)-SC:O(1)
        axorb = reduce(lambda a,b: a^b,nums)
        k = self.right_most_setbit(axorb)
        a = 0
        for item in nums:
            if item & (1 << k):
                a ^= item
        b = axorb^a
        return a,b
