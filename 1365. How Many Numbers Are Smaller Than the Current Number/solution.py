from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashtable = {}
        nums_sorted = sorted(nums)
        prev = -1
        for idx, item in enumerate(nums_sorted):
            if prev != item:
                hashtable[item] = idx
            prev = item
        return [hashtable[item] for item in nums]

if __name__ == "__main__":
    soln = Solution()
    assert str(soln.smallerNumbersThanCurrent([8,1,2,2,3])) == str([4,0,1,1,3])
    assert str(soln.smallerNumbersThanCurrent([6,5,4,8])) == str([2,1,0,3])
    assert str(soln.smallerNumbersThanCurrent([7,7,7,7])) == str([0,0,0,0])
    print("Passed all test cases!")