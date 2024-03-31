class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        k = []
        n = len(arr)

        for idx in range(n):
            maxNum = max(arr[:n-idx])
            maxIdx = arr.index(maxNum)+1
            arr[:maxIdx] = reversed(arr[:maxIdx])
            k.append(maxIdx)
           
            arr[:n-idx] =  reversed(arr[:n-idx])
            k.append(n-idx)
        
        return k
        