class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0] )
        count = 1
        currRange = points[0][1] 
        print(points)

        for i in range(1, len(points)):
            if currRange < points[i][0]:
                count+=1
                currRange = points[i][1]
                continue
            currRange =  min(currRange, points[i][1])
            
        return count

        