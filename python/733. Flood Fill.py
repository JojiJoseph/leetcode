import sys

sys.setrecursionlimit(100_000_000)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        image[sr][sc] = newColor
        if sr>=1:
            if image[sr-1][sc] == color:
                self.floodFill(image, sr-1, sc, newColor)
        if sr<m-1:
            if image[sr+1][sc] == color:
                self.floodFill(image, sr+1, sc, newColor)
        if sc>=1:
            if image[sr][sc-1] == color:
                self.floodFill(image, sr, sc-1, newColor)
        if sc<n-1:
            if image[sr][sc+1] == color:
                self.floodFill(image, sr, sc+1, newColor)
        return image
