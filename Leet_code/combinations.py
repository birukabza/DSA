class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = []

        def backtrack(idx, nums):
            if len(nums) == k:
                res.append(nums.copy())
                return
            
            for i in range(idx, n+1):
                
                backtrack(i+1, nums + [i])
                
            
        backtrack(1,nums)

        return res

            
                     