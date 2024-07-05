from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        res = [[float("inf") for _ in range(col)] for _ in range(row)]
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r,c):
            return 0<=r<row and 0<=c<col
        
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))


        while queue:
            for _ in range(len(queue)):
                r, c =queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if inbound(nr, nc) and res[nr][nc] == float("inf"):
                        res[nr][nc] = res[r][c] + 1
                        queue.append((nr, nc))

        return res
        