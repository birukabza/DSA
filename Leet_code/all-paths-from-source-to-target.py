class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(node, curr):
            curr.append(node)
            if node == len(graph)-1:
                res.append(curr[:])
            
            for nei in graph[node]:
                dfs(nei, curr)
                curr.pop()
        
        dfs(0,[])
        return res


        