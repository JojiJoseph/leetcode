# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        arr = []
        while node:
            arr.append(node)
            node = node.next
        i, j = 0, len(arr)-1
        while i<=j:
            arr[i].next = arr[j]
            if i + 1 < j:
                arr[j].next = arr[i+1]
            i += 1
            j -= 1
        arr[len(arr)//2].next = None
        return head
