class NumArray:

    def __init__(self, nums: list[int]):
        self.prefixSum = [0]*(len(nums)+1)

        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] = self.prefixSum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]