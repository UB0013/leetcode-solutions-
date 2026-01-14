class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        top = 0 
        bottom = len(matrix)-1
        l = 0
        r = len(matrix[0])-1

        while l < r: 
            for i in range (r-l):
                topleft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i] [l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topleft
            l = l+1
            r = r -1 
            top = top +1
            bottom = bottom -1

        