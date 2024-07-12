from heapq import heappop, heappush


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minHeap = []

        for i in range(n):
            heappush(minHeap, [matrix[i][0], i , 0])
        
        while k > 0 and minHeap:
            k-=1
            val, i, j = heappop(minHeap)

            if j+1 < n:
                heappush(minHeap, [matrix[i][j+1],i,j+1])

        return val

