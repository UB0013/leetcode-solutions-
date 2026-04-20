class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq1 = [0]*26 
        freq2 = [0]*26 

        for c in s1 : 
            freq1[ord('a')- ord(c)] += 1 
        l = 0 
        r = 0 
        for r in range (len(s2)): 
            freq2[ord('a') - ord(s2[r])] += 1  
            if r-l+1 > len(s1): 
                freq2[ord('a') - ord(s2[l])] -= 1  
                l = l +1 
            if freq1 == freq2 :
                return True 
        return False
