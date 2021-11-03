# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedUtil(self, root):
        if not root:
            return 0
        height_left = self.isBalancedUtil(root.left)
        if height_left == -1:
            return -1
        height_right = self.isBalancedUtil(root.right)
        if height_right == -1:
            return -1
        elif abs(height_left-height_right) <= 1:
            return 1 + max(height_left,height_right)
        else:
            return -1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return not self.isBalancedUtil(root) == -1
