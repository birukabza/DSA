from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        state = [[0]*n for _ in range(m)]

        guard = 1
        wall = 2
        guardedCell = 3

        for x, y in guards:
            state[x][y] = guard
        
        for x,y in walls:
            state[x][y] = wall
        
        #going from left to  right
        for r in range(m):
            currentState = 0
            for c in range(n):
                if state[r][c] == guard:
                    currentState = guardedCell 
                elif state[r][c] == wall:
                    currentState = 0 
                else:
                    if currentState == guardedCell:
                        state[r][c] = guardedCell
        
        #going from right to left
        for r in range(m):
            currentState = 0
            for c in range(n-1, -1 , -1):
                if state[r][c] == guard:
                    currentState = guardedCell 
                elif state[r][c] == wall:
                    currentState = 0 
                else:
                    if currentState == guardedCell:
                        state[r][c] = guardedCell
        
        #going from top to bottom
        for c in range(n):
            currentState = 0
            for r in range(m):
                if state[r][c] == guard:
                    currentState = guardedCell 
                elif state[r][c] == wall:
                    currentState = 0
                else:
                    if currentState == guardedCell:
                        state[r][c] = guardedCell
        
        #going from bottom to top
        for c in range(n):
            currentState = 0
            for r in range(m-1, -1, -1):
                if state[r][c] == guard:
                    currentState = guardedCell 
                elif state[r][c] == wall:
                    currentState = 0
                else:
                    if currentState == guardedCell:
                        state[r][c] = guardedCell
        
        countUnguarded = 0
        for x in range(m):
            for y in range(n):
                if state[x][y] == 0:
                    countUnguarded+=1
        
        return countUnguarded






        
        
