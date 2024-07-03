class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        row = len(image)
        col = len(image[0])
        checker = image[sr][sc]

        if checker == color:
            return image
        def inbound(r,c):
            return 0<=r<row and 0<=c<col
         
        def dfs(r,c):
            image[r][c] = color
            for dr, dc in directions:
                new_r = r+dr
                new_c = c+dc
                if (inbound(new_r, new_c) and 
                    image[new_r][new_c] == checker):
                    dfs(new_r, new_c)
        dfs(sr,sc)
        return image