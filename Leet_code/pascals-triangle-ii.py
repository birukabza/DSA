class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prevRow = self.getRow(rowIndex-1)

        currentRow = [1]

        for i in range(1, rowIndex):
            currentRow.append(prevRow[i-1] + prevRow[i])
        
        currentRow.append(1)
    
        return currentRow
