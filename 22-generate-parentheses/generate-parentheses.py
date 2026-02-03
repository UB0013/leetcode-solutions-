class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openN = 0 
        closeN = 0 
        res = []
        stack = []
        def dfs (openN,closeN):
            if openN == closeN == n :
                res.append("".join(stack))
             
            if openN< n :
                stack.append("(") 
                dfs (openN+1,closeN)
                stack.pop()
            if closeN<openN:
                stack.append(")")
                dfs (openN, closeN+1)
                stack.pop()
        dfs (0,0)
        return res 

        