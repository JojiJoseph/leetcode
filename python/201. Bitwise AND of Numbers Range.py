class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        base = 1
        while left or right:
            if (left & 1) and (right & 1):
                ans += base
            elif (left & 1) != (right & 1):
                ans = 0
            base <<= 1
            left >>= 1
            right >>= 1
        return ans


if __name__ == "__main__":
    soln = Solution()
    
    assert soln.rangeBitwiseAnd(5, 7) == 4
    assert soln.rangeBitwiseAnd(0, 0) == 0
    assert soln.rangeBitwiseAnd(1, 2147483647) == 0
    assert soln.rangeBitwiseAnd(5, 5) == 5

    print("Passed all test cases successfully!")
