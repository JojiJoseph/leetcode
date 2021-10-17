from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0
        self.nodes = []
        self.map = defaultdict(lambda:0)
    
    def pathSumUtil(self, node, targetSum, currentSum):
        if node is None:
            return
        else:
            if self.map[node.val + currentSum - targetSum]:
                self.count+=self.map[node.val + currentSum - targetSum]
            self.map[node.val+currentSum] += 1
            self.pathSumUtil(node.left, targetSum, currentSum + node.val)
            self.pathSumUtil(node.right, targetSum, currentSum + node.val)
            self.map[node.val+currentSum] -= 1
        
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.map[0] = 1
        self.pathSumUtil(root, targetSum, 0)
        return self.count
