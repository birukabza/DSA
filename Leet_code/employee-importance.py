"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        mp = {}

        for e in employees:
            mp[e.id] = e
        
        def dfs(eid):
            nonlocal res
            e = mp[eid]
            res += e.importance 
            
            for sub in e.subordinates:
                dfs(sub)
        
        dfs(id)
        return res

        