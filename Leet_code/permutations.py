class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(i):
            if i >= len(nums):
                return [[]]
            
            perms = backtrack(i+1)
            res = []
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            
            return res
        
        return backtrack(0)




        
        


        