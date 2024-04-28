class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)
        counter = 0
        p1 = 0
        p2 = 0

        while p2<m:
            if p1 < n and name[p1] == typed[p2]:
                counter+=1
                p1+=1
                p2+=1
            elif p2 > 0 and typed[p2] == typed[p2-1]:
                p2+=1
            else:
                return False      
                
        if counter == n:
            return True
        
        return False 

    
        