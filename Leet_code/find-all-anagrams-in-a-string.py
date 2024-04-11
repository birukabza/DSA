from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        targetCount = Counter(p)
        windowCount = Counter(s[:len(p)-1])

        for i in range(len(p)-1, len(s)):
            windowCount[s[i]] = windowCount.get(s[i], 0) + 1

            if windowCount == targetCount:
                res.append(i - len(p)+1)
            
            windowCount[s[i-len(p)+1]] -= 1

            if windowCount[s[i-len(p)+1]] == 0:
                del windowCount[s[i-len(p)+1]]
               
        return res
        