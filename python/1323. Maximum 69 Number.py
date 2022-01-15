class Solution:
    def maximum69Number (self, num: int) -> int:
        num_s = str(num)
        n = len(num_s)
        for i in range(n):
            if num_s[i] == '6':
                return num_s[:i] + '9' + num_s[i+1:]
        return num
