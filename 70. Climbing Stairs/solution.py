from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n<=0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(19) == 6765
    assert sol.climbStairs(45) == 1836311903
    print("Passed all test cases!")