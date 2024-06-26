class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        def cycleSort(nums):
            n = len(nums)
            i= 0
            while i < n:
                pos = nums[i]
                if pos < n and pos!=i:
                    nums[pos], nums[i] = nums[i], nums[pos]
                else:
                    i+=1
            return nums
        
        nums = cycleSort(nums)

        for i,n in enumerate(nums):
            if i!=n:
                return i
        return len(nums)

