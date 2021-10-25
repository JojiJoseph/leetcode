from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetricUtil(self, left, right):
        if left == right == None:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.isSymmetricUtil(left.left, right.right) and self.isSymmetricUtil(left.right, right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricUtil(root, root)
