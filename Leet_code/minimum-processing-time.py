from typing import List
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        min_time = 0
        j=3
        for i in range(len(processorTime)):
            min_time = max(min_time, processorTime[i]+tasks[j])
            j+=4

        return min_time
            

        