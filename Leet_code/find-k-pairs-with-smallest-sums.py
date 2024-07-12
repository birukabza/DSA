from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for i in range(min(len(nums2), k)):
            heappush(minHeap, (nums1[0] + nums2[i], 0, i))
        
        while minHeap and k > 0:
            k-=1
            _, i, j = heappop(minHeap)

            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heappush(minHeap, (nums1[i+1] + nums2[j], i+1, j))
        
        return res

