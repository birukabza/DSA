class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        upperBound = sum(weights)
        lowerBound = max(weights)
        res = upperBound
        currentSum = 0
        daysTaken = 1

        while lowerBound < upperBound:
            candidate = (lowerBound+upperBound)//2

            for w in weights:
                currentSum+=w
                if currentSum > candidate:
                    daysTaken+=1
                    currentSum = w
            
            if daysTaken > days:
                lowerBound = candidate + 1
            else:
                res = min(res, candidate)
                upperBound = candidate
            
                
            currentSum = 0
            daysTaken = 1

            
        return res