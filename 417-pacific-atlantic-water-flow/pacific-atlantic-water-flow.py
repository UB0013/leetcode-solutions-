class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = []
        atlantic = []
        visitedpacific = [[False] * cols for  n in range(rows)]
        visitedatlantic = [[False]* cols for n in range(rows)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))

        def bfs (ocean,visit):
            q = deque(ocean)

            while q : 
                r, c = q.popleft()
                visit[r][c] = True 
                for mr , mc in directions:
                    nr = r+ mr 
                    nc = c + mc
                    if nr < 0 or nc<0 or nr >= rows or nc >= cols or heights[nr][nc] < heights[r][c] or visit[nr][nc] == True  :
                        continue
                    q.append((nr,nc))



        bfs(pacific,visitedpacific)
        bfs (atlantic,visitedatlantic)

        res =[]

        for r in range(rows):
            for c in range(cols):
                if visitedpacific[r][c] and visitedatlantic[r][c]:
                    res.append((r,c))

        return res 


        