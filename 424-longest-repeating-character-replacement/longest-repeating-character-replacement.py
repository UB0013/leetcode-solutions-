class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        
        l  = 0 
        r = 0 
        res = 0 
            

        while r in range (len (s)): 
            freq[s[r]] = 1+ freq.get(s[r],0)
            if r-l+1 - max(freq.values()) > k :
                freq[s[l]] -= 1
                l = l +1
            res = max(res,r-l+1)
            r = r+1
        return res




        


        