from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = max(piles)
        lowerBound = 1
        hrTaken = 0

        while lowerBound < upperBound:
            candidate = (lowerBound + upperBound) //2

            for p in piles:
                hrTaken += ceil(p/candidate)
            
            if hrTaken > h:
                lowerBound = candidate + 1
            else:

                upperBound = candidate 

            hrTaken = 0
        
        return upperBound
    



        