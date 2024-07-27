class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            backtrack(i+1, curr+[nums[i]])

            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            backtrack(i+1, curr)
    
        nums.sort()
        backtrack(0, [])

        return res