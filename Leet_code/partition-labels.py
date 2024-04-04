class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        res =[]
        end = 0
        size = 0
        for i in range(len(s)):
            size+=1
            end = max(end, d[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res
                
        