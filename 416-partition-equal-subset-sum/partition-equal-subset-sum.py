class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 ==1 :
            return False
        dp = set ()
        dp.add(0)
        target = sum(nums)//2 
        n = len(nums)
        for i in nums : 

            newdp = set ()
            for x in dp:
                if target in dp :
                    return True 
                newdp.add (x + i)
                newdp.add(x)

            dp = newdp 

        return False
       