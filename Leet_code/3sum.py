class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n-2):
            if 0 < i < n-2 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = n-1
            while j <k:
                if nums[i]+ nums[j] + nums[k]==0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1 
                elif nums[i]+ nums[j] + nums[k]>0:
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1 
                else:
                    j+=1
                    while i<j<k and nums[j] == nums[j-1]:
                        j+=1
                        
        return res
