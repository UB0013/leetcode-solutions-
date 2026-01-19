class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands =0 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        if not grid :
            return 0 
        def dfs (r,c) :
            grid[r][c] = "0"
            for mr , mc in directions:
                nr = mr + r 
                nc = mc + c
                if nr >=0 and nc >=0 and nr < rows and nc < cols and grid[nr][nc] == "1":
                    dfs (nr,nc)
             



        for r in range (rows):
            for c in range(cols):
                if grid[r][c] == "1" :
                    dfs (r,c)
                    islands += 1 
        return islands 

        