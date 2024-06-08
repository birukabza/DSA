from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = defaultdict(int)
        runningSum = 0

        for n in nums:
            runningSum+=n

            if runningSum-k == 0:
                res+=1
            
            res += prefixSum[runningSum-k]
            prefixSum[runningSum]+=1
        
        return res
            

        