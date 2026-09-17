# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle
        slow, fast = head, head


        # slow finds the middle + 1 element
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        # reverse the second half
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        # merge the two last
        second = prev
        first = head
        while second:
            temp = first.next
            first.next= second
            temp2 = second.next
            second.next = temp

            first = temp
            second = temp2

        
            
        