class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = {}
        countt = {}

        l, r  = 0 , 0 
        reslen  =  float("inf")
        have = 0 
        res = [-1,1]

        for c in t : 
            countt[c] = 1 + countt.get (c,0) 
        need = len (countt)

        while r < len(s) :
            counts[s[r]] = 1 + counts.get(s[r],0)
            if s[r] in countt and counts[s[r]] == countt[s[r]]:
                have = have + 1 
            while have == need : 
                if r-l+1 < reslen : 
                    res = s[l:r+1]
                    reslen = r-l+1 
                counts[s[l]]  -= 1 
                if s[l] in countt and counts[s[l]] < countt[s[l]] : 
                    have -= 1 
                l = l+1 
            r = r + 1 
        return res if reslen !=  float("inf") else ""

