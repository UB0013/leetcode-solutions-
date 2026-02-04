class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        count = 0 


        def dfs (r,c) :
            grid[r][c] = "0" 
            for mr , mc in directions :
                nr = r+mr
                nc = c + mc 
                if nr>= 0 and nc >=0 and nr < rows and nc < cols and grid[nr][nc] == "1":
                    dfs(nr,nc) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" : 
                    dfs (r,c)
                    count = count + 1 
        return count 


        