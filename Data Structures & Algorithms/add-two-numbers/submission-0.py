# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            if l1:
                s1 = l1.val
            else:
                s1  = 0
            if l2:
                s2 = l2.val
            else:
                s2 = 0
            
            sum = s1 + s2 + carry
            carry = 0
            if sum >= 10:
                sum = sum % 10
                carry = 1
            
            res.next = ListNode(sum)
            res = res.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            

        
        return dummy.next

            