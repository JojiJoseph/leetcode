# class Solution:
#     def findComplement(self, num: int) -> int:
#         complement = 0
#         bits = 0
#         while num:
#             complement = complement + ((1-(num&1)) << bits);
#             bits += 1
#             num >>= 1
#         return complement

class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            num ^= i
            i <<= 1
        return num
