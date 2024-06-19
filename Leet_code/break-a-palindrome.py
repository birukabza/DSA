class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n ==1:
            return ""
        res = ""
        
        for i in range(n//2):
            if palindrome[i]!="a":
                res = palindrome[:i] + "a" + palindrome[i+1:]
                break
        
        if res:
            return res
        else:
            return palindrome[:n-1]+"b"
