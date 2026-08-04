# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        while head != None:
            res.append(head.val)
            head = head.next

        
        l,r = 0,len(res) - 1
        while l < r:
            if res[l] == res[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True