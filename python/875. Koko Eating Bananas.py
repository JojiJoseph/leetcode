class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        low = sum(piles)//h
        if low == 0:
            low = 1
        high = ans
        while low <= high:
            mid = (low + high)//2
            hours = 0
            for p in piles:
                hours += ceil(p / mid)
            if hours > h:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
