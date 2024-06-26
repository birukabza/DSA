from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        sortedList = SortedList()
        res = 0

        for n in instructions:
            i = sortedList.bisect_left(n)
            j = sortedList.bisect_right(n)
            greater = len(sortedList)-j
            lesser  = i
            res+=min(greater, lesser)
            res%=MOD
            sortedList.add(n)
        
        return res

        