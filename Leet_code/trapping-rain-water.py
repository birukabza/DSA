class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n
        maxL = height[0]
        for i in range(1, n):
            max_left[i] = maxL
            maxL = max(maxL, height[i])
            
        max_right = [0]*n
        maxR = height[n-1]
        for i in range(n-1, -1, -1):
            max_right[i] = maxR
            maxR = max(maxR, height[i])
        
        water_trapped = 0

        for i in range(n):
            if min(max_left[i], max_right[i]) - height[i] > 0:
                water_trapped+= min(max_left[i], max_right[i]) - height[i]
        
        return water_trapped
            



        
        
        