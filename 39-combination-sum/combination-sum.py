class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res =[]
        stack = []
        

        def dfs (i, stack,stacksum):
            if stacksum == target :
                res.append(stack.copy())
                return 
            if i >= len(candidates) or  stacksum > target : 
                return 
            stack.append(candidates[i])
            #stacksum += candidates[i]
            dfs (i,stack,stacksum + candidates[i])
            #removed = stack.pop()
            #stacksum -= removed 
            stack.pop()
            dfs(i+1,stack,stacksum)

        dfs (0,stack,0)
        return res  
            

        