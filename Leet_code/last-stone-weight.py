from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        for i in range(len(stones)):
            stones[i]*=-1
        heapify(stones)
        

        while len(stones) > 1:
            s1 = -heappop(stones)
            s2 = -heappop(stones)

            if s1 > s2:
                heappush(stones, -(s1-s2))
            else:
                pass
        
        return -stones[0] if stones else 0


                
