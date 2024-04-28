class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countW = 0
        start = 0
        min_recolor = float("inf")

        for end in range(len(blocks)):
            if blocks[end] == "W":
                countW+=1

            if end - start + 1 == k:
                min_recolor = min(min_recolor, countW)
                if blocks[start] == "W":
                    countW-=1
                start+=1
        
        return min_recolor

            
                    
        
        