from random import randint
from typing import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        unique = list(counter.keys())
        

        def quickSelect(left, right, k):
            if left >= right:
                return
            pivot_idx = randint(left, right)

            pivot = counter[unique[pivot_idx]]
            unique[pivot_idx], unique[right] = unique[right], unique[pivot_idx]
            holder = left
            for i in range(left, right):
                if counter[unique[i]] > pivot:
                    unique[holder], unique[i] = unique[i], unique[holder]
                    holder+=1

            unique[right], unique[holder] = unique[holder], unique[right]
            if k == holder:
                return
            elif k > holder:
                quickSelect(holder+1, right, k)
            else:
                quickSelect(left, holder-1, k)
                

        quickSelect(0, len(unique)-1, k-1)
        return unique[:k]
        
        