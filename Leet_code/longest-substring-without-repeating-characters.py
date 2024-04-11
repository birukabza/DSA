class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        visited = {}
        max_substring = 0

        while end < len(s):

            if s[end] in visited and start <= visited[s[end]]:
                start = visited[s[end]]+1
            
            visited[s[end]] = end
            
           
            max_substring = max(max_substring, end-start+1)
            end+=1
        
        return max_substring

