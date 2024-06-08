class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[2])
        n = trips[-1][2]
        diff = [0]*(n+1)

        for numPass, fromI, toI in trips:
            diff[fromI] += numPass
            diff[toI] -= numPass
         
        for i in range(1, n):
            diff[i] += diff[i-1] 
            if diff[i] > capacity:
                return False

        if diff[0] > capacity:
            return False

        return True        