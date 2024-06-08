class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles and target >1:
            if target%2:
                count+=1
                target-=1
                continue
            target /=2
            maxDoubles-=1
            count+=1
        
        if target > 1:
            count+=(target-1)
        
        return int(count)
        


        