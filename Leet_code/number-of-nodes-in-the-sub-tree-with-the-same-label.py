from collections import Counter, defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        res = [0]*n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        def dfs(node, parent):
            counter = Counter()
            counter[labels[node]]+=1

            for child in graph[node]:
                if child != parent:
                    child_counter = dfs(child, node)
                    counter+=child_counter
     
            res[node] = counter[labels[node]]
            
            return counter
        

        dfs(0, -1)
        return res