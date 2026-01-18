class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board  = [["."]*n for i in range(n) ]
        row = set()
        cols = set()
        posdiag =set()
        negdiag =set()
        res =[]

        def dfs (r):
            if r == n :
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range (n):
                if c in cols or c+r in posdiag or c-r in negdiag :
                    continue 
                cols.add(c)
                posdiag.add(c+r)
                negdiag.add(c-r)
                board[r][c] = "Q"
                dfs (r+1)
                cols.remove(c)
                posdiag.remove(c+r)
                negdiag.remove(c-r)
                board[r][c] = "."
        dfs(0)
        return res 


        