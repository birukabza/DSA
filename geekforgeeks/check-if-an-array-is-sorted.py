#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
