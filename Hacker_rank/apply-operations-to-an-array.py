class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                i+=2
            else:
                i+=1
        j = 0
        k = 0
        while j < n:
            if nums[j]!=0:
                nums[k], nums[j] = nums[j], nums[k]
                k+=1
            j+=1
        return nums
        