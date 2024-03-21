class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        row = len(matrix)
        col = len(matrix[0])
        res = [[0]*row for _ in range(col)]
        for i in range(col):
            for j in range(row):
                res[i][j] = matrix[j][i]
        return res        