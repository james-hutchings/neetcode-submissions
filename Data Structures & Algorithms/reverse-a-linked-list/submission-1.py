# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create current and set to head.
        prev = None 
        curr = head

        # While current:
        while (curr):

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev