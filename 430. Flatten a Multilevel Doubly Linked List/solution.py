"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flattenUtil(self, head):
        if not head:
            return None, None
        node = head
        head.prev = None
        prev = None
        while node:
            if node.child:
                first, last = self.flattenUtil(node.child)
                node.next, last.next = first, node.next
                first.prev = node
                if last.next:
                    last.next.prev = last
                node.child = None
                node = last
            if node:
                prev = node
            node = node.next
        return head, prev
    
    def flatten(self, head: 'Node', end=None) -> 'Node':
        head, last = self.flattenUtil(head)
        return head
