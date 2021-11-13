from functools import reduce
class Solution:
    def add(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        num3 = ""
        n = len(num1)
        m = len(num2)
        carry = 0
        for i, j in zip(num1,num2):
            i = int(i)
            j = int(j)
            k, carry = (i+j+carry)%10, (i+j+carry)//10
            num3 += str(k)
        if n > m:
            for i in num1[m:]:
                k = int(i) + carry
                num3 += str(k % 10)
                carry = k // 10
        elif m > n:
            for i in num2[n:]:
                k = int(i) + carry
                num3 += str(k % 10)
                carry = k // 10
        if carry:
            num3 += str(carry)
        return num3[::-1]
    def scale(self, num1, k):
        num1 = num1[::-1]
        num3 = ""
        carry = 0
        for d in num1:
            d = int(d)*k + carry
            d, carry = d % 10, d // 10
            num3 += str(d)
        if carry:
            num3 += str(carry)
        return num3[::-1]
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        nums = []
        for idx, ch in enumerate(num2[::-1]):
            nums.append( self.scale(num1, int(ch)) + "0"*idx)
        ans = reduce(self.add, nums)
        return ans

if __name__ == "__main__":
    soln = Solution()

    assert soln.multiply("2", "3") == "6"
    assert soln.multiply("123", "456") == "56088"
    assert soln.multiply("1234", "0") == "0"
    assert soln.multiply("0", "456") == "0"
    
    print("Passed all test cases!")