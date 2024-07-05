from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid)
        directions = [(0,1), (0, -1), (1,0), (-1,0)]

        def inbound(r, c):
            return 0 <= r< row and 0 <= c < col
        
        visited = set()
        def bfs1(r , c):
            visited.add((r, c))
            queue = deque([(r, c)])
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc]:
                            visited.add((nr, nc))
                            queue.append((nr,nc))
        def bfs2(r, c):
            queue = deque(visited)
            level = 0
            while queue:
                level += 1
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if inbound(nr, nc) and (nr, nc) not in visited:
                            if grid[nr][nc]:
                                return level-1
                            visited.add((nr, nc))
                            queue.append((nr,nc))

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    bfs1(i,j)
                    return bfs2(i, j)   


        