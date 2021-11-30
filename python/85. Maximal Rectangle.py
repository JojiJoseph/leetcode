from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        i_matrix = [[0]*m for i in range(n)]
        for row in range(n):
            cols_s = 0
            for col in range(m):
                if matrix[row][col] == '1':
                    i_matrix[row][col] = int(matrix[row][col]) + (col>0) * i_matrix[row][col-1]
        largest_area = 0
        for row in range(n):
            for col in range(m):
                if i_matrix[row][col] != 0:
                    width = i_matrix[row][col]
                    for k in range(row, n):
                        width = min(width, i_matrix[k][col])
                        area = width*(k-row+1)
                        if area > largest_area:
                            largest_area = area
                            if area == 0:
                                break
        return largest_area
