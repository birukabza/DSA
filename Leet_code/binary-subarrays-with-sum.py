from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        runningSum = defaultdict(int)
        count = 0
        prefixSum = 0

        for num in nums:
            prefixSum+=num

            if prefixSum - goal in runningSum:
                count += runningSum[prefixSum - goal]
            
            if prefixSum == goal:
                count+=1
            
            runningSum[prefixSum]+=1
        
        return count


        


