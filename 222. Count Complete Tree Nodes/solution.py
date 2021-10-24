from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def height(self, root):
        if root:
            return 1 + self.height(root.left)
        return 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h = self.height(root)
        hr = self.height(root.right)
        if  hr == h-1:
            return (1 << (h-1)) + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + (1<<hr)
