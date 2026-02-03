class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res =[]
        stack =  []

        def dfs (stack , total, i ) :
            if total == target :
                res.append(stack.copy())
                return 
            if i >= len(candidates) or total > target :
                return 
            stack.append(candidates[i])
            dfs (stack,total+candidates[i], i+1)
            stack.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i +1]:
                i  = i+1
            dfs (stack,total,i+1)
        dfs (stack,0,0)
        return res 
        