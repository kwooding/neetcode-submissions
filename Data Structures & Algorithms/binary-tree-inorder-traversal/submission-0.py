# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return []
        
        def dfs(node):
            if node is None:
                return None
            dfs(node.left)

            res.append(node.val)

            dfs(node.right)

            return res

        
        res = dfs(root)
        return res

        