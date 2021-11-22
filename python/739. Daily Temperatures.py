from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                ans[stack[-1][1]]= i - stack[-1][1]
                stack.pop()
            stack.append((t,i))
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert str(sol.dailyTemperatures([73,74,75,71,69,72,76,73])) == str([1,1,4,2,1,1,0,0])
    assert str(sol.dailyTemperatures([30,40,50,60])) == str([1,1,1,0])
    assert str(sol.dailyTemperatures([30,60,90])) == str([1,1,0])
    print("Passed all test cases!")