class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        item = 1
        row = [1]
        for i in range(rowIndex):
            item = item * (rowIndex-i)//(i+1)
            row.append(item)
        return row
