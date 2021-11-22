# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterUtil(self, root) -> (int, int):
        if not root:
            return 0, 0
        left_height, left_dia = self.diameterUtil(root.left)
        right_height, right_dia = self.diameterUtil(root.right)
        height = max(left_height, right_height) + 1
        rooted_dia = left_height + right_height
        return height, max(rooted_dia, left_dia, right_dia)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, dia = self.diameterUtil(root)
        return dia
