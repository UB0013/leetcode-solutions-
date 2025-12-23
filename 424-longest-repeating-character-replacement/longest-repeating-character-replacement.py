class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0 
        res = []
        reslen =0 

        freq = {}

        for r in range (len (s)) :
            freq[s[r]] = 1 + freq.get(s[r], 0)
            if (r-l+1 ) - max(freq.values()) > k:
                freq[s[l]] -= 1 
                l = l+1
            reslen = max(r-l+1,reslen)
            r = r+1
            
        return reslen 
         
        