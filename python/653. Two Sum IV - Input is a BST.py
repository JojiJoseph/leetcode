# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        q = deque()
        q.append(root)
        while len(q):
            node = q.pop()
            if node:
                if (k - node.val) in nums:
                    return True
                nums.add(node.val)
                q.append(node.left)
                q.append(node.right)
        return False
