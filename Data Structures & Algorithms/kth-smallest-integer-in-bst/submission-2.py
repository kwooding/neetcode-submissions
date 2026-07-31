# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node,res=[]):
            if node is None:
                return None
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

            return res

        print(inorder(root))
        return inorder(root)[k-1]