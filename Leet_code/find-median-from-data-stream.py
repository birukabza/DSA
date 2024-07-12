from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)

        if self.maxHeap and self.minHeap:
            if -self.maxHeap[0] > self.minHeap[0]:
                val = -heappop(self.maxHeap)
                heappush(self.minHeap, val)
        
        if len(self.maxHeap) > len(self.minHeap) +1:
            val = -heappop(self.maxHeap)
            heappush(self.minHeap, val)
        
        if len(self.minHeap) > len(self.maxHeap) +1:
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -val)
        
    def findMedian(self) -> float:

        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        else:
            return  (self.minHeap[0] +   -self.maxHeap[0]) /2  
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()