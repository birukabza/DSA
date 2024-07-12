class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def helper(i, j):
            if i > j:
                return 0
            
            pick_i = nums[i] - helper(i+1, j)
            pick_j = nums[j] - helper(i, j-1)

            return max(pick_i, pick_j)
        
        res = helper(0, len(nums)-1)

        return res >= 0

        
            
        