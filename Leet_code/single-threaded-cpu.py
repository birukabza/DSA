from heapq import heappop, heappush
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()
        res = []
        minHeap = []
        i = 0
        time = 0

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i+=1
            
            if minHeap:
                taken, idx = heappop(minHeap)
                time += taken
                res.append(idx)
            else:
                time = tasks[i][0]

        
        return res
        

        