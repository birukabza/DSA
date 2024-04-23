from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = 9, 9
        # Checking for the rows
        for row in board:
            visited = set()
            for num in row:
                if num.isdigit():
                    if num in visited:
                        return False
                    else:
                        visited.add(num)

        # Checking for the columns
        for i in range(cols):
            visited = set()
            for row in board:
                if row[i].isdigit():
                    if row[i] in visited:
                        return False
                    else:
                        visited.add(row[i])
        
        # Checking for the 3x3 grids
        for i in range(0, 9, 3):
            for j in range(0,9,3):
                visited = set()
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y].isdigit():
                            if board[x][y] in visited:
                                return False
                            else:
                                visited.add(board[x][y])

        return True


