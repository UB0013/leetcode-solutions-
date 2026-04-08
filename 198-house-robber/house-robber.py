class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len (nums)
        dp = [0]*n 

        if n > 1 : 

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])


            for i in range(2,n,1) :
            #print (i)
                dp[i] = max (dp[i-1], dp[i-2]+nums[i])

            return dp[n-1] 
        else :
            return nums[0]




        