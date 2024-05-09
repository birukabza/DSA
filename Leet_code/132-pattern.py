class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = [] 
        minimums = [nums[0]]
        currMin = nums[0]
        

        for n in nums[1:]:
            while stack and n > stack[-1]:
                stack.pop()
                minimums.pop()
            
            if stack and n < stack[-1] and  n > minimums[-1]:
                return True
            
            stack.append(n)
            minimums.append(currMin)
            currMin = min(currMin, n)


        return False


        