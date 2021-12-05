# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, root):
        """
        Returns max_if_include, max_if_not_included
        """
        if not root:
            return 0, 0
        if root.left == root.right == None:
            return root.val, 0
        a,b = self.util(root.left)
        c,d = self.util(root.right)
        
        return b+d+root.val, max(a,b)+max(c,d)
    def rob(self, root: Optional[TreeNode]) -> int:
        a, b = self.util(root)
        return max(a,b)
  