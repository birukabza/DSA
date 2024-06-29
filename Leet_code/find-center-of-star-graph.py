from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for n, val in graph.items():
            if len(val) == len(edges):
                return n

        