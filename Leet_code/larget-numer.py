from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums[:] = [str(n) for n in nums]

        def compare(x, y):
            if x+y > y+x:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums)))