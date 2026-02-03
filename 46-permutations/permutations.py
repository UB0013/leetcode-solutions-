class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        included = [False] * len(nums)
        stack =[]
        res = [] 
        def dfs ():
            if len(stack)== len(nums) :
                res.append(stack.copy())
                return
            for i in range (len(nums)):
                if included[i] == True : 
                    continue 
                stack.append(nums[i])
                included[i] = True 
                dfs ()
                stack.pop()
                included[i] =False 
        dfs ()
        return res 
            

