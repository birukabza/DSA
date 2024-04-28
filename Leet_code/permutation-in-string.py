from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_counter = Counter(s1)
        window_counter = Counter(s2[:len(s1)-1])
        left = 0

        for right in range(len(s1)-1, len(s2)):

            window_counter[s2[right]] = window_counter.get(s2[right], 0)+1

            if window_counter == target_counter:
                return True
            
            if window_counter[s2[left]] == 1:
                del window_counter[s2[left]]
            else:
                window_counter[s2[left]]-=1
            
            left+=1
        
        return False



