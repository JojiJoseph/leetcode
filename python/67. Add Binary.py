class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(b) > len(a):
            a = "0"*(len(b)-len(a)) + a
        else:
            b = "0"*(len(a)-len(b)) + b
        a = reversed(a)
        b = reversed(b)
        ans = ""
        carry = 0
        for x, y in zip(a,b):
            x = ord(x)-ord('0')
            y = ord(y)-ord('0')
            z = x+y+carry
            carry = 1 if z > 1 else 0
            if z&1:
                ans +="1"
            else:
                ans += "0"
        if carry:
            ans += "1"
        return ans[::-1]
