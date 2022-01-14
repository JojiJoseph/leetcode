class Solution:
    def myAtoi(self, s: str) -> int:
        state_start = 0
        state_leading_space = 1
        state_sign_neg = 2
        state_sign_pos = 3
        state_digit = 4
        number = 0
        state = state_start
        sign = 1
        for ch in s:
            flag = False
            if ch == " ":
                if state == state_start or state == state_leading_space:
                    state = state_leading_space
                else:
                    number = sign*number
                    return min(max(number, - (1<<31)), (1<<31)-1)
            elif 0 <= ord(ch)-ord('0') <= 9:
                number = number * 10 + ord(ch)-ord('0')
                state = state_digit
            elif ch == "-":
                if state == state_start or state == state_leading_space:
                    sign = -1
                    state = state_sign_neg
                else:
                    flag = True
            elif ch == '+':
                if state == state_start or state == state_leading_space:
                    sign = 1
                    state = state_sign_neg
                else:
                    flag = True
            else:
                number = sign * number
                return min(max(number, - (1<<31)), (1<<31)-1)
            if flag or sign*number < -(1<<31) or sign*number > (1<<31)-1:
                number = sign * number
                return min(max(number, - (1<<31)), (1<<31)-1)
        number = sign * number
        return min(max(number, - (1<<31)), (1<<31)-1)
