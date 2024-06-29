class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dest = set()
        res = []

        for u, v in edges:
            dest.add(v)
        
        for i in range(n):
            if i not in dest:
                res.append(i)
        
        return res
          
        