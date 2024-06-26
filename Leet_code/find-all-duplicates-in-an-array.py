class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        def cycleSort(nums):
            n = len(nums)
            i= 0
            while i < n:
                pos = nums[i] - 1
                if nums[pos]!=nums[i]:
                    nums[pos], nums[i] = nums[i], nums[pos]
                else:
                    i+=1
                
            return nums
        cycleSort(nums)

        for i,n in enumerate(nums):
            if i+1!=n:
                res.append(n)
        return res

        