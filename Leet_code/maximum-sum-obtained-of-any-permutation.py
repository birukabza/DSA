class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        diff = [0]*(len(nums)+1)
        res = 0
        MOD = 10**9 + 7

        for start, end in requests:
            diff[start]+=1
            diff[end+1]-=1
        
        for i in range(1,len(diff)):
            diff[i] = diff[i-1] + diff[i]
        
        nums.sort(reverse = True)
        diff.sort(reverse = True)

        for i in range(len(nums)):
            res+= ((nums[i]*diff[i])%MOD)


        return res%MOD

        
        