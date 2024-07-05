# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if (not root.left and not root.right):
            return []
        if k == 0:
            return [target.val]
        graph = defaultdict(list)

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
        queue = deque([target])
        visited = set([target])
        level = 0
        res = []
        flag = True
        while queue and flag:
            level +=1
            
            for _ in range(len(queue)):
                node = queue.popleft()

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            while level == k and queue:
                node  = queue.popleft()
                res.append(node.val)
                flag = False
           

        return res
            




        
        