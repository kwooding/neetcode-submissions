# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = 0,0
        dummy = head
        curr = dummy
        seen = set()
        while curr is not None:
            print(curr)
            if curr not in seen:
                seen.add(curr)
            else:
                return True
            curr = curr.next

        return False
        