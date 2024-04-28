class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counter = Counter(t)
        window_counter = {}
        res = [-1, -1]
        res_len = float("inf")
        start = 0
        current = 0

        for end in range(len(s)):
            if s[end] in target_counter:
                window_counter[s[end]] = window_counter.get(s[end], 0) +1
            
            if s[end] in target_counter and window_counter[s[end]] == target_counter[s[end]]:
                current+=1
            
            while current == len(target_counter):
                
                if end-start+1 <= res_len:
                    res = [start, end+1]
                res_len = min(res_len, end-start+1)
                if s[start] in target_counter:
                    window_counter[s[start]]-=1
                    if window_counter[s[start]] < target_counter[s[start]]:
                        current-=1
                start+=1
        
        return s[res[0]: res[1]]








        
            
            
        