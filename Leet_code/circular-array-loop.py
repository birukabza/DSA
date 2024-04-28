class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        slow, fast = -1, -1

        def next(current_idx: int) -> int:
            return (current_idx + nums[current_idx])%n
        
        for i in range(n):
            slow = i
            fast = next(i)

            while nums[i] * nums[fast] > 0 and nums[i]*nums[next(fast)] > 0:
                if slow == fast:

                    if slow == next(slow):
                        break

                    return True
                
                slow = next(slow)
                fast = next(next(fast))
        
        return False
                




