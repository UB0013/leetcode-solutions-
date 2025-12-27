class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0 
        r = 0 
        sett = set ()
        res = 0 
        while r < len (s) : 
            
            if s[r] not in sett : 
                sett.add(s[r])
                r = r+1 
                res = max(res,len(sett)) 
            else : 
                while s[r] in sett : 
                    sett.remove (s[l])
                    l = l+1 
        return res 

# l = 0 
# r= 1

# sett = [ab ]

        