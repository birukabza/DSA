class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def cycleSort(nums):
            n = len(nums)
            i= 0
            while i < n:
                pos = nums[i] - 1
                if 0<=pos<n and nums[pos]!=nums[i]:
                    nums[pos], nums[i] = nums[i], nums[pos]
                else:
                    i+=1
                
            return nums
        cycleSort(nums)

        for i,n in enumerate(nums):
            if i+1!=n:
                return i+1
        return len(nums)+1
    
# #this is the first solution I came up with but uses extra spaceclass Solution:
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         set_nums = set(nums)

#         for i in range(1, len(nums)+1):
#             if i not in set_nums:
#                 return i
#         return len(nums) +1