class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def merge(left, right):
            res = []
            j = 0
            nonlocal count
            for l in left:
                while j < len(right) and l > right[j]*2:
                    j+=1
                count += j
                
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            
            while i < len(left):
                res.append(left[i])
                i+=1
            
            while j < len(right):
                res.append(right[j])
                j+=1
            
            return res
        
        def mergeSort(nums, s, e):
            if s>=e:
                return [nums[s]]
            
            m = s + (e-s)//2
            left = mergeSort(nums, s, m)
            right = mergeSort(nums, m+1,e)

            return merge(left, right)

        mergeSort(nums, 0, len(nums)-1)
        
        return count