class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = [] 
        subset = []
        total = 0 

        def dfs (i,total):
            if total == target :
                result.append(subset.copy())
                return 
            if total > target :
                return 
            if i >= len(candidates):
                return  
            subset.append(candidates[i])
            dfs (i,total+candidates[i])
            subset.pop()
            dfs (i+1,total)
        dfs (0,0)
        return result 
            



        