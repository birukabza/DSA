"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res = 0
        if not root:
            return 0

        def dfs(node, curr):
            nonlocal res
            if not node.children:
                res = max(res, curr)
                return

            curr+=1
            for child in node.children:
                dfs(child,curr)
        
        dfs(root,1)
        return res

