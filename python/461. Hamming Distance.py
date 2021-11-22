class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        dist = 0
        while z:
            z &= (z-1)
            dist += 1
        return dist
