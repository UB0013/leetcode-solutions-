class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len (matrix[0])
        #3 rows 
        #4 cols


        l = 0
        r= rows-1
        ROW = 0 
        while l<=r :
            mid = (l+r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][cols-1]:
                    ROW = mid
                    break 
            elif target > matrix[mid][cols-1] : 
                l =mid+1 
            elif target < matrix[mid][0]:
                r = mid-1
        print (ROW)
        

        l = 0 
        r = cols-1 


        while l <= r : 
            mid = (l+r)//2
            if matrix[ROW][mid ] == target:
                return True 
            elif target > matrix[ROW][mid]:
                l = mid +1 
            else :
                r = mid-1 
        return False 

        






        