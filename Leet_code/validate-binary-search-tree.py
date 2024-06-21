# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, lBoundary, rBoundary):
            if not node:
                return True
            
            if not (lBoundary < node.val < rBoundary):
                return False
            
            left = validate(node.left, lBoundary, node.val)
            right = validate(node.right, node.val, rBoundary)

            return left and right
        
        return validate(root, float("-inf"), float("inf"))
        
