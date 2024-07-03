class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,-1), (0, 1)]
        count = 0
        row = len(grid1)
        col = len(grid1[0])
        visited= set()


        def inbound(r,c):
            return 0<=r<row and 0<=c<col

        def dfs(r,c):
            visited.add((r,c))
            flag = True
            if grid1[r][c]!=grid2[r][c]:
                flag = False
            

            for dr, dc in directions:
                nr = r + dr
                nc = c +dc
                if (inbound(nr, nc) and 
                    (nr, nc) not in visited 
                    and grid2[nr][nc]):
                    if not dfs(nr,nc):
                        flag = False
            return flag

            
        
        for i in range(row):
            for j in range(col):
                if grid2[i][j] and (i,j) not in visited:
                    if dfs(i,j):
                        count+=1
        return count

        