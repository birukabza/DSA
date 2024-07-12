from collections import defaultdict


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # so I want to remove some subarray such that their mod is equal to the sum(nums)%p
        # if i keep all the mods with one pass and check if the mod of one subbary minus the other equal to sum(nums)%p then it can be one of the answers
        # some what similar to leetcode 974
        res = len(nums)
        mod = defaultdict(int)
        mod[0] = -1 #this handles the case when we want to remove a subarray when it starts from the beginning
        target = sum(nums)%p
        runningSum = 0

        if sum(nums)%p == 0:
            return 0
        
        for i, n in enumerate(nums):
            runningSum+=n
            currMod = runningSum%p

            if (currMod - target + p)%p in mod: # +p not a problem in python but in other lang it is a must
                j = mod[(currMod - target + p)%p ]
                res = min(res, i - j)

            mod[currMod] = i
        
        return res if res!=len(nums) else -1

        
