from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0
        graph = defaultdict(set)

        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        

        for i in range(n):
            for j in range(i+1, n):
                total = len(graph[i]) + len(graph[j])
                currRank = total if i not in graph[j] else total-1
                maxRank = max(maxRank, currRank)
        return maxRank



        