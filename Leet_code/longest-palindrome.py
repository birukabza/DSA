from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        extra = False
        cnt = 0

        for c in counter:
            if counter[c]%2 == 0:
                cnt += counter[c]
            elif counter[c] > 1:
                cnt += counter[c] - 1
                extra = True
            else:
                extra= True
        
        return cnt + 1 if extra else cnt

        