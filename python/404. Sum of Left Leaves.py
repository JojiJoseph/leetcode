# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeavesUtil(self, root, parent_from):
        if not root:
            return 0
        if root.left == root.right == None and parent_from == 0:
            return root.val
        return self.sumOfLeftLeavesUtil( root.left, 0) + self.sumOfLeftLeavesUtil( root.right, 1)
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sumOfLeftLeavesUtil(root, 1)
