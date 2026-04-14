class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapp = {}

        l = 0 
        r = 0
        final_result = 0 

        
        for r in range (len(s)): 
            mapp[s[r]] = 1 + mapp.get(s[r], 0)
            max_freq = max(mapp.values()) #O(n)
            len_curr = r-l+1
            result = len_curr-max_freq
            while (r - l + 1) - max_freq  > k :
                mapp[s[l]] =  mapp[s[l]] - 1 
                l = l +1 
            #print (final_result ) 
            final_result = max(r-l+1 ,  final_result) 
        return final_result
        
            


            
            










            

            



        