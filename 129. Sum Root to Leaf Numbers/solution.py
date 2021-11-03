# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbersUtil(self, root, number):
        if not root:
            return 0
        elif root.left == root.right == None:
            return number*10 + root.val
        else:
            return self.sumNumbersUtil(root.left, number*10 + root.val) + self.sumNumbersUtil(root.right, number*10 + root.val)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sumNumbersUtil(root, 0)
