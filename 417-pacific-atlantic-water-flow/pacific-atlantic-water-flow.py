class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len (heights)
        cols = len (heights[0])
        atlanticvisit = [[False] * cols for _ in range (rows) ]
        pacificvisit = [[False] * cols for _ in range (rows) ]
        pacific = []
        atlantic = []
        res = [] 
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        for r in range (rows)  :
            pacific.append ((r,0))
            atlantic.append((r,cols-1))
            pacificvisit[r][0] = True
            atlanticvisit[r][cols-1] = True 
        for c in range (cols):
            pacific.append((0,c))
            atlantic.append ((rows-1,c)) 
            pacificvisit[0][c] = True
            atlanticvisit [rows-1][c] = True 

        def bfs (ocean,visit) :
            q = deque (ocean)
            while q : 
                r, c = q.popleft ()
                for mr , mc in directions :
                    nr = r + mr 
                    nc = c + mc 
                    if nr <0 or nc < 0 or nr >= rows or nc >= cols or heights[nr][nc] < heights[r][c] or visit[nr][nc]  :
                        continue 
                    q.append((nr,nc))
                    visit[nr][nc] = True 
            


        bfs (pacific, pacificvisit)
        bfs (atlantic,atlanticvisit)


        

        for r in range (rows) :
            for c in range (cols) : 
                if pacificvisit[r][c] and atlanticvisit[r][c] : 
                    res.append ((r,c))
        return res 

          

    
            
        