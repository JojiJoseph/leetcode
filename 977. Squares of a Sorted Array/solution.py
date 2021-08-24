from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x*x for x in nums]
        n = len(nums)
        prev = nums[0]
        i = 0
        while prev >= nums[i] and i < n-1:
            prev = nums[i]
            i += 1
        i -= 1
        j = i+1
        new_arr = []
        while i >= 0 or j < n:
            if j < n and i >= 0 and nums[j] < nums[i]:
                new_arr.append(nums[j])
                j += 1
            elif i >= 0 and j < n and nums[i] <= nums[j]:
                new_arr.append(nums[i])
                i -= 1
            elif i >= 0:
                new_arr.append(nums[i])
                i -= 1
            else:
                new_arr.append(nums[j])
                j += 1
        return new_arr

if __name__ == "__main__":
    solution = Solution()
    assert str(solution.sortedSquares([-4,-1,0,3,10])) == str([0,1,9,16,100])
    assert str(solution.sortedSquares([-7,-3,2,3,11])) == str([4,9,9,49,121])
    assert str(solution.sortedSquares([-3,-2,-1])) == str([1,4,9])
    assert str(solution.sortedSquares([5])) == str([25])
    assert str(solution.sortedSquares([1,2,3])) == str([1,4,9])
    print("Passed all test cases!")