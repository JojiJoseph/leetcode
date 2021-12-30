class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        ans = 1
        rep = 1 % k
        md_set = set()
        while rep != 0:
            rep = (rep*10 + 1) % k
            if rep != 0 and rep in md_set:
                return -1
            md_set.add(rep)
            ans += 1
        return ans
