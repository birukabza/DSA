class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        op = 0
        i, j = 0, len(nums)-1

        while i < j:
            if nums[i]+nums[j]==k:
                op+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]>k:
                j-=1
            else:
                i+=1
        
        return op
        