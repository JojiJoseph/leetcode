class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_count = [0]*n
        out_count = [0]*n
        for a, b in trust:
            in_count[b-1] += 1
            out_count[a-1] += 1
        for i, (ic, oc) in enumerate(zip(in_count, out_count)):
            if ic == n-1 and oc == 0:
                return i+1
        return -1
