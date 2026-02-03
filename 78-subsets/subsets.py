class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []

        i=0 

        def dfs (stack, i):
            if i == len (nums) :
                res.append(stack.copy())
                return 
            stack.append(nums[i])
            dfs(stack,i+1)
            stack.pop()
            dfs (stack,i+1)
        dfs (stack,0)
        return res 
