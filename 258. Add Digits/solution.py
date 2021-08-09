class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
if __name__ == "__main__":
    sol = Solution()
    assert sol.addDigits(38) == 2
    assert sol.addDigits(0) == 0
    assert sol.addDigits(75) == 3
    assert sol.addDigits(32) == 5
    assert sol.addDigits(59) == 5
    print("Passed test cases")