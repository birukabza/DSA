from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1, -1), (-1,1)]
        n = len(grid)

        def inbound(r,c):
            return 0<=r<n and 0<=c<n
        
        queue = deque([(0,0)])
        visited = set([(0,0)])
        level = 0

        while queue:
            level+=1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                if grid[r][c] == 1:
                    continue

                if r == n-1 and c== n-1:
                    return level

                for dr, dc in directions:
                    nr,nc = dr+r, dc + c

                    if inbound(nr, nc) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr,nc))
        
        return -1
            
