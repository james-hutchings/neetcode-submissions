# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize two pointers, have them move through each list, check if curr exists and which is greater. 

        curr1 = list1
        curr2 = list2
        dummy = ListNode()
        built = dummy

        while (curr1 and curr2):
            if (curr1.val < curr2.val): 
                built.next = curr1
                curr1 = curr1.next
                built = built.next

            else: 
                built.next = curr2
                curr2 = curr2.next
                built = built.next

        while (curr1):
            built.next = curr1
            curr1 = curr1.next
            built = built.next

        while (curr2):
            built.next = curr2
            curr2 = curr2.next
            built = built.next

        return dummy.next