# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        while list1 is not None or list2 is not None:
            if list1 is None:
                res.next = list2
                res = res.next
                list2 = list2.next
            elif list2 is None:
                res.next = list1
                res = res.next
                list1 = list1.next
            elif list1.val < list2.val:
                res.next = list1
                res = res.next
                list1 = list1.next
            else:
                res.next = list2
                res = res.next
                list2 = list2.next

        return dummy.next