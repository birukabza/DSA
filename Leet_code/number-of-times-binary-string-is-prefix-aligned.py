class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        count = 0
        n = len(flips)
        max_idx = 0
        
        for i in range(n):
            max_idx = max(max_idx, flips[i])

            if max_idx == i+1:
                count+=1

        return count

