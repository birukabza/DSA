from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        res = ""
        diff = [0] * (n + 1)
        
        for sh in shifts:
            if sh[2]:
                diff[sh[0]]+=1
                diff[sh[1]+1]-=1
            else:
                diff[sh[0]]-=1
                diff[sh[1]+1]+=1
        
        for i in range(1,n):
            diff[i]+=diff[i-1]
        
        for i in range(n):
            char = chr((ord(s[i]) - ord('a') + (diff[i]))%26 + ord('a') )
            res+=char

        return res

            
            