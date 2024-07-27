class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, curr, s):
            if s == target:
                res.append(curr[:])
                return
            if s > target:
                return
            if i >= len(candidates):
                return
            
            backtrack(i+1, curr + [candidates[i]], s + candidates[i])
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, curr, s)

        candidates.sort()
        backtrack(0, [], 0)
        
        return res