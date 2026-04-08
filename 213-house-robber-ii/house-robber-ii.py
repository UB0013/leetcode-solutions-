class Solution:
    def rob(self, nums: List[int]) -> int:
        n =len (nums)

        if n ==1 :
            return nums[0]

        def helper(nums) : 
            x = len (nums)
            if x ==1 :
                return nums[0]

            dp = [0] * x 
            dp[0] = nums[0]
            dp[1] = max (dp[0],nums[1])

            for i in range (2,x):
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            return dp[x-1]



        result = max (helper(nums[0:n-1]), helper(nums[1:]))

        return result

        