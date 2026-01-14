class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        cols = len(matrix[0])
        
        rows  = len(matrix)
        rowzero =False
        

        for r in range (rows):
            for c in range(cols):
                if matrix[r][c] == 0 and r == 0 :
                    rowzero = True
                if matrix[r][c] ==0 and r > 0 :
                    matrix[r][0] = 0 
                if matrix [r][c] == 0 :
                    matrix[0][c] = 0 
        
        for r in range (1,rows):
            for c in range (1, cols):
                if matrix[0][c] == 0 :
                    matrix[r][c] = 0 
                if matrix[r][0] ==0 :
                    matrix[r][c] =0 
        if matrix[0][0] ==0 :
            for r in range(rows):
                matrix[r][0] = 0 
      
        if rowzero == True :
            for i in range(cols):
                matrix[0][i] = 0 
        


       

        