from collections import Counter
import math


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        res = 0

        for ans in counter:
            res+= (math.ceil(counter[ans]/(ans+1))) * (ans+1)
               
        return res
        
        