from collections import defaultdict


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = defaultdict(lambda: -1)

        for num in nums2:
            while stack and num > stack[-1]:
                res[stack[-1]] = num
                stack.pop()

            stack.append(num)
        
        return [res[num] for num in nums1]