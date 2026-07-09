# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # placeholder head, discarded at the end
        current = dummy      # pointer that builds the merged list

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1   # link the smaller node
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next     # advance the builder pointer

    # attach whichever list still has nodes
        current.next = list1 if list1 is not None else list2

        return dummy.next
            