from typing import List


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            if mid+1 <= right and arr[mid]==arr[mid+1] and (n-mid) % 2 == 0:
                right = mid-1
            elif mid+1 <= right and arr[mid]==arr[mid+1]:
                left = mid+2
            elif mid-1 >= left and arr[mid]==arr[mid-1] and (n-mid)%2 == 0:
                left = mid+2
            elif mid-1 >= left and arr[mid]==arr[mid-1]:
                right = mid-2
            else:
                return arr[mid]
        return arr[right]
