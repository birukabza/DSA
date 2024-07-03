from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = [-1]*(n+1)

        def dfs(node):

            for nei in graph[node]:
                if color[nei] == color[node]:
                    return  False
                elif color[nei] == -1:
                    color[nei] = 1-color[node]
                    if not dfs(nei):
                        return False
            return True

        for i in range(1,n+1):
            if color[i]==-1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True        
            
        
       