from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, item in enumerate(sorted(nums)) if item == target]
