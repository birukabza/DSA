class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        numToIdx = [(n, i) for i, n in enumerate(nums)]

        def merge(left, right):
            merged = []
            i = 0
            j = 0
            count = 0
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    res[left[i][1]] += count
                    merged.append(left[i])
                    i+=1
                else:
                    count+=1
                    merged.append(right[j])
                    j+=1
            
            while i < len(left):
                res[left[i][1]] += count
                merged.append(left[i])
                i+=1
            
            while j < len(right):
                merged.append(right[j])
                j+=1
            
            return merged
        
        def mergeSort(pairs, s, e):
            if s>=e:
                return [pairs[s]]
            
            m = s + (e-s)//2
            left = mergeSort(pairs, s, m)
            right = mergeSort(pairs, m+1,e)

            return merge(left, right)

        mergeSort(numToIdx, 0, len(nums)-1)
        return res
            