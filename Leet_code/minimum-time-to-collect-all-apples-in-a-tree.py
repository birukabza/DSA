from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, par):
            time = 0
            for child in graph[node]:
                if child != par:
                    curr = dfs(child, node)
                    if curr or hasApple[child]:
                        time += curr + 2
            return time

        return dfs(0, None)
