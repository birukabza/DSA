class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)

        stack = []
        res = [-1] * n

        for i in range(n*2):
            while stack and nums[i%n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i%n]
            
            stack.append(i%n)
            
        
        return res
        