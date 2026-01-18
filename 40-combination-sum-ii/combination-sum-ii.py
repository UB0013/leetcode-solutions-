class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        candidates.sort()

        def dfs (i, stack, stacksum):
            if stacksum ==target :
                res.append(stack.copy())
                return 
            if i >= len(candidates) or stacksum > target:
                return 
            stack.append(candidates[i])
            dfs (i+1, stack, stacksum+candidates[i])
            stack.pop()
            while i+1  < len (candidates) and candidates[i] == candidates[i+1]:
                i = i +1 
            dfs (i+1,stack,stacksum)
        dfs (0,stack,0)
        return res
        