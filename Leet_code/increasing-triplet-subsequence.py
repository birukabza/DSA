class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        num1 = float("inf")
        num2 = float("inf")
        
        for n in nums:
            if n > num2:
                return True
            
            if n > num1:
                num2 = min(n, num2)
            
            num1 = min(num1, n)
        
        return False
            

        