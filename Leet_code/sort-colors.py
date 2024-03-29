class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)

        for i in range(len(nums)):
            if red > 0:
                nums[i]=0
                red-=1
            elif white > 0:
                nums[i]=1
                white-=1
            elif blue>0:
                nums[i]=2
                blue-=1
        



        