from math import gcd
from typing import Counter, List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = list(Counter(deck).values())

        gcd_ = counter[0]


        for c in counter[1:]:
            gcd_ = gcd(gcd_, c)
        
        return gcd_!=1
        
        