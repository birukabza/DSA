# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node, minVal, maxVal):
            if not node:
                return
            nonlocal res 
            res = max(res, abs(minVal-node.val), abs(maxVal-node.val))
            traverse(node.left, min(minVal, node.val), max(maxVal, node.val))
            traverse(node.right, min(minVal, node.val), max(maxVal, node.val))
        traverse(root, root.val, root.val)
        return res
        
        