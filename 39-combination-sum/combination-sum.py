class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack =[]
        i = 0
        res =[]
        def dfs (stack,total,i):
            if total == target :
                res.append(stack.copy())
                return 
            if i >= len(candidates) or total > target :
                return  
            stack.append(candidates[i])
            dfs (stack,total + candidates[i], i)
            stack.pop()
            dfs (stack,total,i+1)
        dfs (stack,0,0)
        return res 
        