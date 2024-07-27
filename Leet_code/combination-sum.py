class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, curr, s):
            if s == target:
                res.append(curr[:])
                return
            if s > target:
                return
            if i >= len(candidates):
                return
            
            backtrack(i, curr + [candidates[i]], s + candidates[i])
            backtrack(i+1, curr, s)
        
        backtrack(0, [], 0)
        
        return res
        
