class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        visited = set()
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col
        def backtrack(i, j, curr):
            if curr == len(word):
                return True
            if not inbound(i, j) or (i,j) in visited or board[i][j]!=word[curr]:
                return False
            visited.add((i, j))
            for dx, dy in directions:
                nx = i+dx
                ny = j+dy
                if backtrack(nx, ny, curr + 1):
                    return True
            visited.remove((i,j))
            return False
        
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0):
                    return True
        return False