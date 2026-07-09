# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        p1 = head
        for i in range(n):
            p1 = p1.next
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while p1:
            p1 = p1.next
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next

