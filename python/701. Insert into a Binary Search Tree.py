# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = root
        prev = None
        while node:
            if node.val < val:
                prev, node = node, node.right
            else:
                prev, node = node, node.left
        if prev.val < val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root
