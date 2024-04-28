class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        min_length = float("inf")
        currentSum = 0

        for end in range(len(nums)):
            currentSum+=nums[end]

            while currentSum >= target:
                min_length = min(min_length, end-start+1)
                currentSum-=nums[start]
                start+=1
            
        return min_length if min_length!= float("inf") else 0



        