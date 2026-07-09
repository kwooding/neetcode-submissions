"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        if root is None:
            return []

        def dfs(node):
            if node is None:
                return None
            
            if node.children:
                for child in node.children:
                    dfs(child)

            res.append(node.val)


        dfs(root)
        return res