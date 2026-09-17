# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1

        if n == length:
            return head.next        
        # nodo da eliminare:

        curr = head
        for i in range(length - n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head

            