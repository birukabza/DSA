from typing import List 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        res= []
        for n in arr2:
            count_n = arr1.count(n)
            for _ in range(count_n):
                res.append(n)
        left=[]
        for num in arr1:
            if num not in arr2_set:
                left.append(num)

        left.sort()
        res.extend(left)
        return res
    


        