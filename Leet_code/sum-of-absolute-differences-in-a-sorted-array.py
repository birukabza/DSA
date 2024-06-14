class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        prefixSum = [0]*n
        prefixSum[0] = nums[0]

        for i in range (1, n):
            prefixSum[i] = prefixSum[i-1]+nums[i]
        
        for i in range(n):
            if i == 0:
                res[i] = abs((nums[i]*(n-i-1)) - (prefixSum[n-1] - prefixSum[i]))
                continue
            res[i] = ((nums[i]*i) - prefixSum[i-1]) + abs((nums[i]*(n-i-1)) - (prefixSum[n-1] - prefixSum[i]))

        return res