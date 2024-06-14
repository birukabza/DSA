class Solution:
    def maxScore(self, s: str) -> int:
        maxSum = s.count("1")
        

        res = 0
        countZero = 0
        countOne = 0

        for c in s[:len(s)-1]:
            if c == "0":
                countZero+=1
            else:
                countOne+=1
            
            res = max(res, countZero+(maxSum-countOne))
        
        return res


                  

        