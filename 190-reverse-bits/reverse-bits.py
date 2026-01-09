class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 

        for i in range (32) :
            # we move the ith bit (32 cuz there are those many positions) - so move each bit 
            # to  
            bit = (n >> i) & 1

            res = res | (bit << (31-i) )
        return res 

        