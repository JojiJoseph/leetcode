class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n:
            ans += n % k
            n //= k
        return ans



if __name__ == "__main__":
    solution = Solution()
    assert solution.sumBase(34, 6) == 9
    assert solution.sumBase(15, 10) == 6
    assert solution.sumBase(32, 9) == 8
    assert solution.sumBase(64, 2) == 1
    print("All test cases are passed")