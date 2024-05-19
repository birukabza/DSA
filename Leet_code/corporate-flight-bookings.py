from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        diff = [0] *(n+1)

        for start, end, seats in bookings:
            diff[start-1]+=seats
            diff[end]-=seats
        
        for i in range(n):
            res[i] = res[i-1] + diff[i]
        
        return res

        


        