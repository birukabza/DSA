from typing import List
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        runningSum = 0
        mod = defaultdict(int)

        for n in nums:
            runningSum+=n

            if runningSum%k == 0:
                res+=1
        
            res+=mod[runningSum%k]
            mod[runningSum%k]+=1
        
        return res

            
        