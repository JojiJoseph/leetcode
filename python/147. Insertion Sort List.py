# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find out the minimum node and set it as the head
        outernode = None
        current = head
        
        while current:
            min_node = current
            parent = None
            node = current
            pre = None
            while node:
                if node.val < min_node.val:
                    parent = pre
                    min_node = node
                pre = node
                node = node.next
            if parent:
                parent.next = min_node.next
                min_node.next = current
                current = min_node
            if not parent:
                current = min_node
            if not outernode:
                outernode = current
                head = current
            else:
                outernode.next = current
                outernode = current
            current = current.next
        return head
