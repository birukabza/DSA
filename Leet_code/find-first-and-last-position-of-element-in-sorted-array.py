class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        res = [-1, -1]

        while l < r:
            m = (l+r)//2
            if nums[m] >= target:
                r = m
            else:
                l = m+1

        if nums[l] == target:
            res[0] = l

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l+r)//2
            if nums[m] > target:
                r = m
            else:
                l = m +1

        if nums[r] == target:
            res[1] = r
        elif nums[r-1] == target:   
            res[1] = r - 1 
        
        return res
        