class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        i = j = 0
        output = []
        while i < n and j < m:
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])
            if left <= right:
                output.append([left, right])
            if firstList[i][1] <= secondList[j][1]:
                i+=1
            else:
                j+=1
        return output
