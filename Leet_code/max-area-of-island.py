class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        max_area = 0
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def inbound(r,c):
            return 0<=r<row and 0<=c<col
        
        def dfs(r,c, curr):
            nonlocal max_area
            max_area = max(max_area, curr)
            visited.add((r,c))
            curr+=1

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (inbound(new_r, new_c) and 
                    (new_r, new_c) not in visited and 
                    grid[new_r][new_c]):
                    dfs(new_r,new_c, curr)
        
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j]:
                    dfs(i,j,0)


        return max_area

        