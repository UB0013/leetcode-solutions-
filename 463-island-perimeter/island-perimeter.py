class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])
        mapp = defaultdict(int)
        perimeter = 0 

        for i in range(rows):
            for j in range (cols) : 
                if grid[i][j] ==1 : 
                    mapp[(i,j)] = 0
                    for mr,mc in directions : 
                        nr = i + mr
                        nc = j + mc 
                        if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1 :
                            mapp [(i,j)] += 1 
        for key, value in mapp : 
            # print(mapp[(key,value)])
            perimeter += 4 - mapp[(key,value)] 
        # print (perimeter)
        # print(mapp)
        return perimeter 

                            




        