class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
    
if __name__ == "__main__":
    soln = Solution()
    assert soln.reverseWords("the sky is blue") == "blue is sky the"
    assert soln.reverseWords("  hello world  ") == "world hello"
    assert soln.reverseWords("a good   example") == "example good a"
    assert soln.reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
    assert soln.reverseWords("Alice does not even like bob") == "bob like even not does Alice"
    print("Passed all the testcases!")