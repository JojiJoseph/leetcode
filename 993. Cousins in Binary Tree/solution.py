# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.xdepth = 0
        self.ydepth = 0
        self.xparent = None
        self.yparent = None
    def isCousinsUtil(self, root, x, y, depth=0, parent=None):
        if root is None:
            return
        if root.val == x:
            self.xdepth = depth
            self.xparent = parent
        elif root.val == y:
            self.ydepth = depth
            self.yparent = parent
        else:
            self.isCousinsUtil(root.left, x, y, depth+1, root)
            self.isCousinsUtil(root.right, x, y, depth+1, root)
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.isCousinsUtil(root, x, y)
        if self.xdepth == self.ydepth and self.xparent != self.yparent:
            return True
        return False
