class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s = 0 
        for i in range(k):
            s += nums[i]
        max_avg = s/k
        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i-k]
            avg = s/k
            max_avg = max(max_avg, avg)
        return max_avg