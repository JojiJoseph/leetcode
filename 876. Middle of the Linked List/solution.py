# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        n = 1
        while node.next is not None:
            node = node.next
            n += 1
        mid = n//2
        node = head
        for i in range(mid):
            node = node.next
        return node