class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0 
        r= 0 
        mapp = {}
        res =0

        while r< len(s):
            c = s[r]
            mapp[s[r]] = 1 + mapp.get(s[r],0)
            while (r-l+1) - max(mapp.values()) > k :
                mapp[s[l]] -= 1 
                l = l +1 
            res = max(res,r-l+1)
            r = r + 1 
        return res 


       