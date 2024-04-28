class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        start = 0
        longestSubarray = float("-inf")
        count = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                count+=1
            
            while count > 1:
                if nums[start] == 0:
                    count-=1
                start+=1
            
            longestSubarray = max(longestSubarray, end-start+1)
        
        return longestSubarray-1

        