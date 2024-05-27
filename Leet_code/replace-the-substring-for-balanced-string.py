class Solution:
    def balancedString(self, s: str) -> int:
        charCount = Counter(s) 
        left = 0
        n = len(s) // 4
        res = float("inf")
        
        for right in range(len(s)):
            charCount[s[right]] -= 1

            while left < len(s) and \
                  charCount.get('W', 0) <= n and \
                  charCount.get('Q', 0) <= n and \
                  charCount.get('E', 0) <= n and \
                  charCount.get('R', 0) <= n:
                res = min(res, right - left + 1)
                charCount[s[left]] += 1
                left += 1
             
        return res