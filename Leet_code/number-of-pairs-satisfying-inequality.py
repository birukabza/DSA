class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        diff_arr = [x-y for x,y in zip(nums1, nums2)]

        def merge(left, right):
            nonlocal count
            res = []
            j = len(right)-1
            for l in reversed(left):
                while j >-1 and l <= right[j] + diff:
                        j-=1
                count+= len(right)-j-1
            i = 0
            j = 0
            while i < len(left)  and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        
        def mergeSort(nums, s, e):
            if s==e:
                return [nums[s]]
            
            m = s + (e-s)//2

            left = mergeSort(nums,s,m)
            right = mergeSort(nums, m+1, e)

            return merge(left, right)


        mergeSort(diff_arr, 0, len(diff_arr)-1)
        return count  


        