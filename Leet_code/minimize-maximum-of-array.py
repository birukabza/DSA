class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        currMax = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            currSum+=nums[i]
            
            currMax = max(currMax, ceil(currSum/(i+1)))
        
        
        return currMax

        