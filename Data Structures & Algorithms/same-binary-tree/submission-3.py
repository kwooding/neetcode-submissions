# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Start with stack so we check the last values that we got
        stack = [(p,q)]
        # Go while stack is not empty
        while stack:
            # retrieve nodes for both trees to compare
            node1,node2 = stack.pop()

            # Checking if both are none if this is the case its the same in both trees
            if not node1 and not node2:
                # Go to next iteration if both are none
                continue
            # If one node is none and the other is not or the values are not the same
            # then we want to return false
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # This is how we iterate until the trees are complete
            # We want to eval left side first since we have LIFO structure
            # then we want to put right on the stack first and then the left nodes
            stack.append((node1.right,node2.right))
            stack.append((node1.left,node2.left))

        return True