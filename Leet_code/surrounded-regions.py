class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        def dfs(r, c):
            flag = True
            if r == 0 or r == row - 1 or c == 0 or c == col - 1:
                flag = False

            visited.add((r, c))
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if inbound(nx, ny) and board[nx][ny] == "O" and (nx, ny) not in visited:
                    if not dfs(nx, ny):
                        flag = False

            return flag

        def convert(r, c):
            board[r][c] = "X"
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if inbound(nx, ny) and board[nx][ny] == "O":
                    convert(nx, ny)

        for i in range(row):
            for j in range(col):
                if (i, j) not in visited and board[i][j] == "O" and dfs(i, j):
                    convert(i, j)
