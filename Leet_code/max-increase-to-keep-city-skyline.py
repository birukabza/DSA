class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rowMax = []
        colMax = []
        res = 0

        for r in grid:
            rowMax.append(max(r))
        
        for c in range(col):
            currMax = 0
            for r in range(row):
                currMax = max(grid[r][c], currMax)

            colMax.append(currMax)
        
        for r in range(row):
            for c in range(col):
                res += min(rowMax[r], colMax[c]) - grid[r][c]
        
        return res
        