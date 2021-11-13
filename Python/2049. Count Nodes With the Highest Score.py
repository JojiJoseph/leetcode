from typing import List


class Solution:
    def enumerateTreeSize(self, root, left_children, right_children, tree_sizes):
        n = len(left_children)
        if root >= n or root == -1:
            return 0
        tree_sizes[root] = 1 + self.enumerateTreeSize(left_children[root], left_children, right_children, tree_sizes) + self.enumerateTreeSize(right_children[root], left_children, right_children, tree_sizes)
        return tree_sizes[root]
        
        
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        left_children = [-1]*n
        right_children = [-1]*n
        tree_sizes = [0]*n
        max_prod = 0
        max_count = 0
        for child, parent in enumerate(parents):
            if parent == -1:
                continue
            if left_children[parent] == -1:
                left_children[parent] = child
            else:
                right_children[parent] = child
        self.enumerateTreeSize(0, left_children, right_children, tree_sizes)
        for root, parent in enumerate(parents):
            remaining=n-1
            prod = 1
            if left_children[root] != -1:
                prod *= tree_sizes[left_children[root]]
                remaining -= tree_sizes[left_children[root]]
            if right_children[root] != -1:
                prod *= tree_sizes[right_children[root]]
                remaining -= tree_sizes[right_children[root]]
            if remaining:
                prod *= remaining
            if prod == max_prod:
                max_count += 1
            elif prod > max_prod:
                max_prod = prod
                max_count = 1
        return max_count


if __name__ == "__main__":
    soln = Solution()
    assert soln.countHighestScoreNodes([-1,2,0,2,0]) == 3
    assert soln.countHighestScoreNodes([-1,2,0]) == 2
    print("Passed all test cases!")
