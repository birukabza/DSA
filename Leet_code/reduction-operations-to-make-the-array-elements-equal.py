from typing import List
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        op = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i-1]!=nums[i]:
                op+=i
        
        return op
        
        
        