class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        i, j = 0, len(skill)-1
        res = 0
        checker = skill[i]+skill[j]

        while i < j:
            res+=(skill[i]*skill[j])
            if checker!=skill[i]+skill[j]:
                return -1
            i+=1
            j-=1
        
        return res



        