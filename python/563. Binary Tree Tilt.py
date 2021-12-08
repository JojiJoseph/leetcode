# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def util(self, root):
        if not root:
            return 0,0
        a,b = self.util(root.left)
        c,d = self.util(root.right)
        return a + c + abs(b-d), b + d + root.val
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans,_ = self.util(root)
        return ans
