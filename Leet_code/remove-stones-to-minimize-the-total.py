from heapq import heapify, heappop, heappush
from math import ceil


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i, p in enumerate(piles):
            piles[i] = -p
        heapify(piles)

        while k:
            k-=1
            stone = -heappop(piles)
            heappush(piles, -ceil(stone/2))
        return -sum(piles)



        