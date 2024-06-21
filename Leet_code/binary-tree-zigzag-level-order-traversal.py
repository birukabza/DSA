# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        values = []
        leftTurn = True

        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()   
                values.append(node.val)      
                    
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if leftTurn:
                res.append(values)
                leftTurn = False
            else:
                res.append(reversed(values))
                leftTurn = True
        return res

        