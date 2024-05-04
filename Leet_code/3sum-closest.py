class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        diff: int = None #for tracking the d/ce b/n the target and the current sum
        closestSum = nums[0] + nums[1] + nums[-1]
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            
            j = i+1
            k = n-1

            while j < k:
                currentSum = nums[i]+ nums[j]+nums[k]
                diff = abs(target-currentSum)

                if diff < abs(target-closestSum):
                    closestSum = currentSum
                
                if currentSum > target:
                    k-=1
                else:
                    j+=1
            
        return closestSum



        