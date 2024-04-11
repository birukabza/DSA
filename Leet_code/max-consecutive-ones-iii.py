class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        countZero = 0
        start = 0
        res = 0

        for end in range (len(nums)):
            if nums[end] == 0:
                countZero+=1
            
            while countZero > k:
                if nums[start] == 0:
                    countZero-=1
                start+=1

            res = max(res, end-start+1)

        return res