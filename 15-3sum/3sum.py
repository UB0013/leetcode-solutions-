class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted (nums) 
        print (nums)
        res = []

        for i, n in enumerate (nums) : 
          
            if i > 0 and nums[i-1] == n  :
                continue 
            l = i +1 
            r = len(nums)-1 
            
            while l<r : 
                if nums [l] + nums [r] + nums [i] == 0 :
                    res.append([nums[l], nums[r], nums[i]])
                    while l < r  and nums[l+1] == nums[l] : 
                        l = l +1 
                    l = l+ 1

                elif  nums [l] + nums [r] + nums [i] >  0 :
                    r = r-1 
                elif  nums [l] + nums [r] + nums [i] <  0 :
                    l = l +1 
        return res 



                




 #-1, -1, 0, 1, 2

    #-1  -1 2


        