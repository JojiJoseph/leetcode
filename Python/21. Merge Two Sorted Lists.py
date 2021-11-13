# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        while True:
            if l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                    node = node.next
                else:
                    node.next = l2
                    l2 = l2.next
                    node = node.next
            elif l1:
                node.next = l1
                break
            else:
                node.next = l2
                break
        return head.next
 