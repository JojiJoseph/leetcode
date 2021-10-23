class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left+right)//2
            sqr = mid*mid
            if sqr == x:
                return mid
            elif sqr > x:
                right = mid-1
            else:
                left = mid+1
        return right
