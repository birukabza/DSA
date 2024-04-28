from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixsum = self.calculateprefix(matrix)
    

    def calculateprefix(self, matrix: List[List[int]]):
        prefix = [[0 for _ in range (len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i in range (1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j]+ prefix[i][j-1] - prefix[i-1][j-1]
        return prefix 
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixsum[row2+1][col2+1] - self.prefixsum[row1][col2+1] - self.prefixsum[row2+1][col1]+ self.prefixsum[row1][col1]
