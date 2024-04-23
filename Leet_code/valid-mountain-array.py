class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        increasing = False
        decreasing = False

        if n < 3:
            return False
        
        for i in range(n-1):
            if arr[i] > arr[i+1]:#indicates it is decreasing
                if not increasing: #this will check if the arrasy was not increasing before it starts to decrease
                    return False
                decreasing = True
            elif arr[i] < arr[i+1]: # indicates it is increasing
                if decreasing: #this will check if the array is decreasing before it starts to increase
                    return False
                increasing = True
            else: # this means they are equal and we dont want any flat surface
                return False
        
        if increasing and decreasing: #if both conditions are met we return True
            return True
        else:
            False
        
        
                

        
        