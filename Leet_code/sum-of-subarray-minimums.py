class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        stack = [-1]
        arr.append(0)
        res = 0

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                subArray = (idx - stack[-1]) * (i - idx)
                res += (subArray*arr[idx])%MOD

            stack.append(i)
        
        return res%MOD