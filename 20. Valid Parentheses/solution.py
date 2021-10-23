class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["$"]
        for ch in s:
            if ch == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif ch == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif ch == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 1

if __name__ == "__main__":
    soln = Solution()
    assert soln.isValid("()") == True
    assert soln.isValid("()[]{}") == True
    assert soln.isValid("(]") == False
    assert soln.isValid("([)]") == False
    assert soln.isValid("{[]}") == True
    print("Passed all test cases!")