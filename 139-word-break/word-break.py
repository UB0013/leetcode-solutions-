class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len (s)
        dp = [False] * (n+1)
        dp[n] = True 

       # LEETCODE

        #[F F F F F F F F T]

        for i in range (n-1 , -1 , -1 ):
            for w in wordDict : 
                lenw = len(w)
                if i + lenw <=n and s[i:i+lenw] == w :
                    dp [i] = dp[i+lenw]
                if dp[i]:
                    break 
        return dp [0]



        