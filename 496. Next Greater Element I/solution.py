from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        stack = []
        for item in nums2:
            while len(stack) and stack[-1] < item:
                prev = stack[-1]
                map[prev] = item
                stack.pop()
            stack.append(item)
        for item in stack:
            map[item] = -1
        return [map[item] for item in nums1]

if __name__ == "__main__":
    solution = Solution()
    assert str(solution.nextGreaterElement([4,1,2],[1,3,4,2])) == str([-1,3,-1])
    assert str(solution.nextGreaterElement([2,4],[1,2,3,4])) == str([3,-1])
    print("Passed all test cases!")
