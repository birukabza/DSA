class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counter = {}
        start = 0

        for end in range(len(s)):
            counter[s[end]] = counter.get(s[end], 0)+1

            if (end-start+1) - max(counter.values()) > k:
                counter[s[start]]-=1
                start+=1
            
            res = max(res, end-start+1)

        return res         
        