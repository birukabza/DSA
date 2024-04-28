class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        start = 0
        currentSum = 0
        maxSum = float("-inf")

        for end in range(len(nums)):
            while start < end and nums[end] in seen:
                seen.remove(nums[start])
                currentSum-=nums[start]
                start+=1

            seen.add(nums[end])
            currentSum += nums[end]
            maxSum = max(maxSum, currentSum)

        return maxSum
