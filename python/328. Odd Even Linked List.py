# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd_head = head
        even_head = head.next
        odd_node = None
        even_node = None
        odd = True
        node = head
        while node:
            if odd:
                if odd_node:
                    odd_node.next = node
                    odd_node = node
                else:
                    odd_node = node
            else:
                if even_node:
                    even_node.next = node
                    even_node = node
                else:
                    even_node = node
            odd = not odd
            node = node.next
        if odd_node:
            odd_node.next = even_head
        if even_node:
            even_node.next = None
        return odd_head
