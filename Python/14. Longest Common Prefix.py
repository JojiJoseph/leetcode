class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for str in strs:
            new_lcp = ""
            for idx, ch in enumerate(str):
                if idx < len(lcp) and ch == lcp[idx]:
                    new_lcp += ch
                else:
                    break
            if new_lcp == "":
                return ""
            lcp = new_lcp
        return lcp
