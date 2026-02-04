class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols =len(grid[0])
        q = deque ()
        time =0 
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        fresh = 0 
        for r in range(rows):
            for c in range(cols) : 
                if grid[r][c] == 1 :
                    fresh += 1 
                if grid[r][c] ==2 :
                    q.append((r,c))
        while q and fresh >0 : 
            for i in range (len(q)):
                r, c = q.popleft()
                for mr, mc in directions :
                    nr = r + mr 
                    nc = c + mc
                    if nr >= 0 and nc >=0 and nr < rows and nc < cols and grid[nr][nc] == 1  :
                        fresh -= 1 
                        grid [nr][nc] =2 
                        q.append((nr,nc))
            time +=1 

        if fresh == 0 : 
            return time 
        else :
            return -1 

            


        

        