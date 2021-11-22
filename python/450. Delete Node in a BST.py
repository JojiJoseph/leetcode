# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSmallestNodeAndRemove(self,root):
        if not root:
            return None
        if not root.left:
            return root
        node = self.getSmallestNodeAndRemove(root.left)
        if root.left == node:
            root.left = node.right
        return node
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if root.left == root.right == None:
                return None
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            node = self.getSmallestNodeAndRemove(root.right)
            root.val = node.val
            if root.right == node:
                root.right = node.right
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
