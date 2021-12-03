import operator
from functools import reduce
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        max_product = max(nums)
        while left < n:
            first_neg_idx = None
            last_neg_idx = None
            i=left
            while i < n:
                if nums[i] == 0:
                    break
                if nums[i] < 0:
                    if first_neg_idx is None:
                        first_neg_idx = i
                    last_neg_idx = i
                i+=1

            if left != i:
                max_product = max(reduce(operator.mul, nums[left:i]), max_product)

            if first_neg_idx is not None:
                if first_neg_idx+1 != i:
                    max_product = max(reduce(operator.mul, nums[first_neg_idx+1:i]), max_product)
                if last_neg_idx != left:
                    max_product = max(reduce(operator.mul, nums[left:last_neg_idx]), max_product)
            left = i+1
        return max_product
