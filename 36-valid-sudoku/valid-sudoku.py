class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        rowset =  defaultdict(set) 
        colset = defaultdict(set)
        squareset = defaultdict (set)

        # rowset[0] = 1 
        # rowset[1].add(2)
        # rowset[1].add(2)
    
        # print (rowset)

      
        for r in range (rows) : # 1
            for c in range(cols) :  # 0  
                
                if board[r][c] == "." :
                    continue
                
                if (board[r][c] in rowset[r] ) or (board[r][c] in colset[c]) or (board[r][c] in squareset[(r//3),(c//3)]) :
                    print(board[r][c])
                    print (rowset[r])
                    print(colset[c])
                    print (squareset[(r//3),(c//3)])

                    return False 
                else :
                    rowset[r].add(board[r][c])
                    colset[c].add(board[r][c])
                    squareset [(r//3),(c//3)].add(board[r][c])
                    
                    
        return True 

