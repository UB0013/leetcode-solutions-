class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt = {}
        counts = {}

        for c in t : 
            countt[c] = 1+ countt.get(c,0)

        need = len (countt)
        reslen = float("inf")

        l = 0 
        r = 0 
        have = 0 

        for r in range (len(s)):
            counts[s[r]] = 1 + counts.get(s[r],0)
            if s[r] in countt and countt[s[r]] == counts[s[r]]:
                have += 1  
            while have == need :
                if r-l+1 < reslen : 
                    res = s[l:r+1]
                    reslen = len(res) 
                counts[s[l]] -= 1 
                if  s[l] in  countt and counts[s[l]] <  countt[s[l]]  : 
                        have -= 1 
                l = l+1
        
        return res if reslen !=  float("inf") else  ""

                



         