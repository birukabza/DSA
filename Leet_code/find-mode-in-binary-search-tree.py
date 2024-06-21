# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        counter = defaultdict(int)
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            counter[node.val]+=1
            dfs(node.right)
        
        dfs(root)

        modeNum = max(counter.values())
        ans = []

        for c in counter:
            if counter[c] == modeNum:
                ans.append(c)
            
        return ans
        