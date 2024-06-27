from math import gcd


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0 
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = gcd(cur, nums[j])
                if cur == k:
                    count +=1
                if cur < k:
                    break
        return count
        