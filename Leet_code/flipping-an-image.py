from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        i = 0
        col = len(image[0])
        for row in image:
            row[:] = row[::-1]
            for i in range(col):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1
        return image

        