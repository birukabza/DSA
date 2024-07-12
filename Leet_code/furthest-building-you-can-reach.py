from heapq import heappop, heappush


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []

        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]


            if diff > 0:
                heappush(maxHeap, -diff)
                bricks -= diff
                if bricks < 0 and ladders > 0:
                    num = -heappop(maxHeap)
                    bricks+=num
                    ladders-=1

                if bricks < 0:
                    return i-1
            
        return len(heights)-1
                
