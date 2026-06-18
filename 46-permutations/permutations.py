class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = [] 
        n= len (nums)
        used = [False] * n 
        print ( used)
        def dfs (i) : 
            if len(subset) == n :
                result.append(subset.copy())
                return 
            for i in range (n): 
                if used[i] : 
                    continue 
                used[i] = True 
                subset.append(nums[i])
                dfs (i+1)
                subset.pop()
                used[i] = False 
        dfs(0)
        return result 










        