class Solution:
    def calculate(self, s: str) -> int:
        n_stack = []
        op_stack = []
        token = 0
        prec = {'+':0,'-':0,'*':1,'/':1}
        for ch in s:
            if '0' <= ch <= '9':
                token = token*10 + ord(ch)-ord('0')
            else:
                if ch == " ":
                    continue
                n_stack.append(token)
                token = 0
                while op_stack and prec[ch] <= prec[op_stack[-1]]:
                    op = op_stack.pop()
                    b,a = n_stack.pop(), n_stack.pop()
                    if op == '+':
                        n_stack.append(a+b)
                    elif op == '-':
                        n_stack.append(a-b)
                    elif op == "*":
                        n_stack.append(a*b)
                    elif op == "/":
                        n_stack.append(a//b)
                op_stack.append(ch)
        n_stack.append(token)
        while op_stack:
            op = op_stack.pop()
            b,a = n_stack.pop(), n_stack.pop()
            if op == '+':
                n_stack.append(a+b)
            elif op == '-':
                n_stack.append(a-b)
            elif op == "*":
                n_stack.append(a*b)
            elif op == "/":
                n_stack.append(a//b)
        return n_stack[0]
