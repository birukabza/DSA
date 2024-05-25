class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        currMax = 1

        for num in arr[1:]:
            if num - currMax > 1:
                currMax+=1
            else:
                currMax = num
        
        return currMax
        