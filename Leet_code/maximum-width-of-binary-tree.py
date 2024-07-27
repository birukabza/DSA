# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        queue = deque([(root, 0, 0)])

        smallest = {}

        while queue:
            node, depth, val = queue.popleft()

            if depth not in smallest:
                smallest[depth] = val
            
            res = max(res, val - smallest[depth]+1)

            if node.left:
                queue.append((node.left, depth+1, val*2))
            
            if node.right:
                queue.append((node.right, depth+1, val*2+1))
                
        return res
            
        