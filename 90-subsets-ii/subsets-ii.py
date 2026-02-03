class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        def dfs (stack,i):
            if i == len(nums):
                res.append(stack.copy())
                return 
            stack.append(nums[i])
            dfs (stack,i+1)
            stack.pop()
            while i+1 < len (nums) and nums[i] == nums[i+1]:
                i = i +1
            dfs (stack,i+1)
        dfs ([],0)
        return res 
        