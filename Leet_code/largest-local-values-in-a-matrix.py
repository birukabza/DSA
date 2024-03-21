class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        res = [[0]*(n-2) for _ in range(n-2)]

        for r in range(n-2):
            for c in range(n-2):
                max_value = 0
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        max_value = max(max_value, grid[i][j])
                res[r][c] = max_value
        return res

        