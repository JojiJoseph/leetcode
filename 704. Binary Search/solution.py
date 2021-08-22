from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert sol.search([-1, 0, 3, 5, 9, 11], 11) == 5
    assert sol.search([-1, 0, 3, 5, 9, 11], -1) == 0
    print("Passed all test cases!")
