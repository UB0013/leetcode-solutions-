class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount 
        dp = [float("infinity")] * (n+1)
        dp[0] = 0 

        for i in range (1,n+1):
            for c in coins :
                if (i - c) >= 0 :
                    dp[i] = min(dp[i], 1 + dp [i-c])

        if dp[n] != float("infinity") :
            return dp [n]
        else :
            return -1 

        

        


