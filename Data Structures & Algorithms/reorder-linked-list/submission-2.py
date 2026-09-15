# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Take linked list, split in half, reverse second half, then alternate every other.
        if not head or not head.next:
            return

        slow = head
        fast = head

        # Finding center using slow and fast.
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # After locating the midpoint:
        prev.next = None

        # Reset previous
        curr = slow
        prev = None

        # Reverse second half. 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Alternate building dummy. 

        # Since first node is always first, skip first l1.
        l1 = head.next
        l2 = prev
        next_is_l1 = False
        curr = head

        while l1 or l2:
            if (not next_is_l1 and l2) or not l1:
                curr.next = l2
                l2 = l2.next
                next_is_l1 = True

            else:
                curr.next = l1
                l1 = l1.next
                next_is_l1 = False

            curr = curr.next



