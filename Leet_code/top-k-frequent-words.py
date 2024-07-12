from collections import Counter
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter =  Counter(words)
        res = []
        min_heap = []
        for x, y in counter.items():
            heappush(min_heap, (y, x))
            if len(min_heap) > k:
                heappop(min_heap)

        while min_heap:
            res.append(heappop(min_heap)[1])

        return res[::-1]
        
       
        