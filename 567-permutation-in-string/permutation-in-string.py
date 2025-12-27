class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freqs1 ={}
        freqs2 ={}
        for c in s1 :
            freqs1[c] = 1+ freqs1.get(c, 0)

        l,r = 0, 0 

        while r < (len(s2)) : 
            freqs2[s2[r]] = 1+ freqs2.get(s2[r], 0 )
            if r-l+1 > len(s1):
                freqs2[s2[l]] -= 1
                #we will have to delete zero frequecies if we sue a dictionary -- not required if using array of 26 
                if freqs2[s2[l]] == 0:
                    del freqs2[s2[l]]
                l= l+1 

            if freqs1 ==freqs2:
                return True 
            r = r + 1 
        return False






        