from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.hashtable = defaultdict(list)
        for idx, item in enumerate(arr):
            self.hashtable[item].append(idx)
        

    def query(self, left: int, right: int, value: int) -> int:
        idx_arr = self.hashtable[value]
        left_idx = bisect_left(idx_arr,left)
        right_idx = bisect_right(idx_arr, right)
        return right_idx - left_idx
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
