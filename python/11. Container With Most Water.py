from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        left, right = 0, n-1
        while left < right:
            area = min(height[left], height[right])*(right-left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1, 1]) == 1
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16
    assert sol.maxArea([1, 2, 1]) == 2
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print("Passed all test cases!")
