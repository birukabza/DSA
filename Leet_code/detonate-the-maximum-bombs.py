from cmath import sqrt


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        res =1

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                distance = sqrt((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2)
                if bombs[i][2]>=distance:
                    graph[i].append(j)
        
        def dfs(node):

            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        
        for node in range(len(bombs)):
            visited = set()
            dfs(node)
            res = max(len(visited), res)

        return res
        