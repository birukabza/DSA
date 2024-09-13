class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row = len(board)
        col = len(board[0])

        directions = [(1, 0), (-1, 0), (0,1), (0, -1), (1, 1), (-1, 1), (1,-1), (-1, -1)]

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        mines = set()

        for i in range(row):
            for j in range(col):
                if board[i][j] == "M":
                    mines.add((i, j))
        
        def dfs(r, c):
            if board[r][c] == "M":
                board[r][c] = "X"
                return 
            count = 0
            if board[r][c] == "E":
                for dx, dy in directions:
                    if (r+dx, c+dy) in mines:
                        count+=1
            if count == 0:
                board[r][c] = "B"
            else:
                board[r][c]= str(count)
                return 


            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if inbound(nx, ny) and board[nx][ny]=="E":
                    dfs(nx, ny)

        
        dfs(click[0], click[1])       
        return board