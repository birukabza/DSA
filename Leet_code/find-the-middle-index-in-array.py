class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        prefixSum= [0]*(len(nums)+1)

        for i in range(1, len(nums)+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
        for i in range(1, len(prefixSum)):
            if prefixSum[i-1] == prefixSum[-1] - prefixSum[i]:
                return i-1
        return -1