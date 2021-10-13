# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorderUtil(self, preorder, left, right):
        if left > right:
            return None
        root = TreeNode(preorder[left])
        root_val = preorder[left]
        i = left+1
        while i <= right and preorder[i] < root_val:
            i += 1
        root.left = self.bstFromPreorderUtil(preorder, left+1, i-1)
        root.right = self.bstFromPreorderUtil(preorder, i, right)
        return root
            
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        return self.bstFromPreorderUtil(preorder, 0, n-1)
