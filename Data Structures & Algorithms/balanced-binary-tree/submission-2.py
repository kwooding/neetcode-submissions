# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.isbalanced = True
        def calc(node):
            if node is None:
                return 0
            
            left = calc(node.left)
            right = calc(node.right)


            if abs(right - left) > 1:
                self.isbalanced = False

            return 1 + max(left,right)
        
        calc(root)
        return self.isbalanced