class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0
        prefixSum = [[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                up = prefixSum[r-1][c] if r > 0 else 0
                left = prefixSum[r][c-1] if c > 0 else 0
                upLeft = prefixSum[r-1][c-1] if min(r, c) > 0 else 0
                prefixSum[r][c] = matrix[r][c] + up + left - upLeft
        
        for r1 in range(rows):
            for r2 in range(r1, rows):
                d = {0:1}
                currSum = 0
                for c in range(cols):
                    up = prefixSum[r1-1][c] if r1 > 0 else 0
                    currSum = prefixSum[r2][c] - up
                    
                    if currSum - target in d:
                        count += d[currSum-target] 

                    d[currSum] = d.get(currSum, 0) + 1

    
        return count
        