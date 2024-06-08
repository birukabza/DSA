class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        upperRange = 0
        count = 0

        for num in nums:
            while upperRange+1 < num:
                count+=1
                upperRange += (upperRange+1)

                if upperRange >= n:
                    return count

            upperRange+=num
            if upperRange >= n:
                return count
  
        while upperRange +1 < n:
            count+=1
            upperRange += (upperRange+1)
        
        return count