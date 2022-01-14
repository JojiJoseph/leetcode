class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        l = 0
        r = 0
        for ch in s:
            if ch == 'L':
                l+=1
            else:
                r+=1
            if l == r:
                ans += 1
        return ans
