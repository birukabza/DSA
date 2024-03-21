class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        res = []
        word1 =  set(words[0])
        for s in word1:
            freq = min([word.count(s) for word in words])
            res+=[s]*freq
        return res        
        