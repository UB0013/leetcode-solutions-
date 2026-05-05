class Solution:
    def numDecodings(self, s: str) -> int:
        n = len (s)
        dp = [0]* (n+1)

        dp[0] = 1
        if s[0] != "0" : 
            dp[1] = 1 
      
        for i in range (2,n+1) :
            if s[i-1] != "0" :
                print("L11")
                dp[i] += dp[i-1]
            if "10" <= s[i-2:i] <= "26" :
                print("L14")
                dp[i] += dp[i-2]
        print(dp)

        return dp[n]
            


        