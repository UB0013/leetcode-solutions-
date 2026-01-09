class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        same = set ()

        l , r = 0 ,0
        res = 0 
        while r < len(s) : 
            while s[r] in same :
                same.remove(s[l])
                l = l + 1 
            same.add(s[r])
            res = max(res, r-l+1 )
            r = r + 1 
        return res 



        