
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum (nums)%2 ==1 :
            return False 
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        n = len(nums)
        for i in nums: 
            newdp = set ()
            for t in dp : 
                if target in dp :
                    return True 
                newdp.add(t + i)
                newdp.add(t)
            dp = newdp 
        
        return False
            


        
       