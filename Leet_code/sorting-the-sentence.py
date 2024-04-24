class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        def compare(y):
            return int(y[-1])
        
        s = sorted(s, key=compare)

        for i in range (len(s)):
            s[i] = s[i][:-1]
            

        return " ".join(s)
        