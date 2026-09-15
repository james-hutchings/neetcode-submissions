# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Iterate through list to certain point, remove at that point. 
        prev = None
        first = head
        second = head

        if not head or not head.next:
            return None
        
        count = 0
        while second and second.next:
            second = second.next
            count += 1

            if count >= n:
                prev = first
                first = first.next
        

        if prev is None:
            return head.next

        prev.next = first.next

        return head