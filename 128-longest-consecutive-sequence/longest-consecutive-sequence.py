class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        print(nums)
        res = 0 


        for n in nums :
            
            if n-1 in nums :
                continue 
            print(n)
            count = 1
            while n + count in nums:
                count =count +1
            res = max(count,res)
        return res

        
        