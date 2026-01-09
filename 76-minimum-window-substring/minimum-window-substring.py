class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt = {}
        counts = {}
        have =0 
        for c in t :
            countt[c] = 1 + countt.get(c,0)
        need= len (countt)

        l =0 
        r= 0 
        res = float("infinity")
        val = [-1,1]

        for r in range (len(s)):
            c= s[r]
            counts[c] = 1 + counts.get(c,0)
            if c in countt and countt[c]==counts[c]:
                have = have+1
            while need == have : 
                if r-l+1 < res :
                    res = r-l+1
                    val = s[l:r+1]
                counts[s[l]] = counts[s[l]]-1
                if s[l] in countt and counts[ s[l] ] < countt [s[l]]:
                    have = have-1
                l = l + 1 
        return val if res != float("infinity") else ""    

  
        
        