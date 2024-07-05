from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1,0), (-1,0), (0, -1), (0,1)]
        row = len(maze)
        col = len(maze[0])

        def inbound(r,c):
            return 0<=r<row and 0<=c<col
        
        queue = ([entrance])
        walls = set()
        exits = set()

        for i in range(row):
            for j in range(col):
                if maze[i][j] == "+":
                    walls.add((i,j))
                
                if (i == 0 or j ==0 or i==row-1 or j == col-1) and [i , j] != entrance:
                    exits.add((i,j))

        distance = 0
        while queue:
            distance+=1
            
            for _ in range(len(queue)):
                r , c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c

                    if inbound(nr,nc) and (nr,nc) not in walls:
                        if (nr, nc) in exits:
                            return distance
                        queue.append([nr, nc])
                        walls.add((nr, nc))
                               
        return -1           





        