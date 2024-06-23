class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(idx, curr):
            
            res.append(curr.copy())
            for i in range(idx, len(nums)):
                backtrack(i + 1, curr+[nums[i]])
                
        

        res = []
        backtrack(0, [])
        return res
