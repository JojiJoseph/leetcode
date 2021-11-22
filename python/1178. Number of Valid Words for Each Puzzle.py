from collections import defaultdict
from typing import List

class Solution:
    def getBitMask(self, word):
        ans = 0
        for ch in word:
            ans |= (1 << (ord(ch)-ord('a')))
        return ans
    
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_masks = [self.getBitMask(word) for word in words]
        mask_count = defaultdict(int)
        for mask in word_masks:
            mask_count[mask]+=1
        ans = []
        for puzzle in puzzles:
            puzzle_mask = self.getBitMask(puzzle)
            first_letter_mask = (1<<ord(puzzle[0])-ord('a'))
            sub_mask = puzzle_mask
            count = 0
            while sub_mask:
                if sub_mask & first_letter_mask:
                    count += mask_count[sub_mask]
                sub_mask = (sub_mask-1) & puzzle_mask
            ans.append(count)
        return ans
                
if __name__ == "__main__":
    sol = Solution()
    assert str(sol.findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"],["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])) == str([1,1,3,2,4,0])
    assert str(sol.findNumOfValidWords(["apple","pleas","please"],["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"])) == str([0,1,3,2,0])
    print("Passed all test cases!")