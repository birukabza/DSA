# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, path):
            nonlocal res
            if not node:
                return
            if len(path) >= 2 and path[-2]%2==0:
                res+=node.val 
            dfs(node.left, path + [node.val])
            dfs(node.right, path + [node.val])
        
        dfs(root, [])
        return res

        