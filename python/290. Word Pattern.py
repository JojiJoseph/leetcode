class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        m = {}
        sep_words = set()
        for ch, word in zip(pattern, words):
            if ch in m:
                if word!=m[ch]:
                    return False
            else:
                m[ch] = word
                if word in sep_words:
                    return False
                else:
                    sep_words.add(word)
        return True
