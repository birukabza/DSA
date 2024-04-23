class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        n = len(matrix)
        i = 0
        j = n -1
        
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for i in range(n):
            matrix[i] = matrix[i][::-1]
            i+=1
        
            
        
                