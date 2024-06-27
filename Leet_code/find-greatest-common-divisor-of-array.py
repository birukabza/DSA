class Solution:
    def findGCD(self, nums: List[int]) -> int:

        max_ = max(nums)
        min_ = min(nums)

        while min_ !=0:
            max_, min_ = min_, max_%min_
        
        return max_


        