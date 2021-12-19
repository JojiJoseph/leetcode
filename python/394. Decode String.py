class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        pre = None
        token = ""
        for ch in s:
            if ch == "[":
                stack.append(int(token))
                token = ""
            elif ch == "]":
                new_str = token*int(stack.pop())
                token = new_str
                while stack and type(stack[-1]) == str:
                    token = stack.pop() + token
            elif "0" <= ch <= "9":
                if not pre or not ("0" <= pre <= "9"):
                    stack.append(token)
                    token = ch
                else:
                    token += ch
            else:
                token += ch
            pre = ch
        stack.append(token)
        return "".join(stack)
