# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = []
        explored = [0]
        stack.append(root)
        paths = []
        while stack:
            node = stack[-1]
            if node.right == node.left == None:
                paths.append("->".join([str(s.val) for s in stack]))
                stack.pop()
                explored.pop()
            else:
                if node.left and explored[-1] == 0:
                    explored[-1] = 1
                    stack.append(node.left)
                    explored.append(0)
                elif node.right and explored[-1] < 2:
                    explored[-1] = 2
                    stack.append(node.right)
                    explored.append(0)
                else:
                    stack.pop()
                    explored.pop()
        return paths
