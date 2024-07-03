from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        row = len(isConnected)
        col = len(isConnected[0])
        provinces= 0
        visited = set()

        for i in range(row):
            for j in range(col):
                if isConnected[i][j]:
                    graph[i].append(j)
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        

        for i in range(row):
            if i not in visited:
                provinces+=1
                dfs(i)
        
        return provinces
        
