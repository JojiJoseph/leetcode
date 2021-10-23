from typing import List
import math

class Solution:
    def findMin(self, nums: List[int], left=0, right=None) -> int:
        if right is None:
            right = len(nums)-1
        if right == -1:
            return math.inf
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return min(self.findMin(nums,left,mid), self.findMin(nums,mid+1,right))
        return nums[left]

if __name__ == "__main__":
    soln = Solution()
    assert soln.findMin([1,3,5]) == 1
    assert soln.findMin([2,2,2,0,1]) == 0
    assert soln.findMin([5,5,5]) == 5
    assert soln.findMin([-40]) == -40
    print("Passed all test cases!")