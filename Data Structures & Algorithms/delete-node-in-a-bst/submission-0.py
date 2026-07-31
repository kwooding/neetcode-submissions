# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        
        if key < root.val:
            # if key is less than value move left
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            # if key is more than value move right
            root.right = self.deleteNode(root.right,key)
        else:
            # if key is equal to our value we want to remove it
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            succ = root.right
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteNode(root.right,succ.val)

        return root