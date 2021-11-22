import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        count = 0
        for word in words:
            if re.search(r"^([a-z]*)([a-z]-[a-z])?([a-z]*)([!\.,])?$", word):
                count += 1
        return count

if __name__ == "__main__":
    soln = Solution()
    assert soln.countValidWords("cat and  dog") == 3
    assert soln.countValidWords("!this  1-s b8d!") == 0
    assert soln.countValidWords("alice and  bob are playing stone-game10") == 5
    assert soln.countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.") == 6
    print("Passed all test cases!")