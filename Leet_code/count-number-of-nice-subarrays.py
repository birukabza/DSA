class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        res = 0
        start = 0
        count = 0
        odd = 0

        for end in range(len(nums)):
            if nums[end]%2!=0:
                count = 0
                odd+=1
            
            while odd == k:
                count+=1
                if nums[start]%2!=0:
                    odd-=1
                start+=1
            
            res+=count


        return res
       