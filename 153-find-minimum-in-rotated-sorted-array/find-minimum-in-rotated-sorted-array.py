class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1 
        while l < r : 
            mid = (l+r)//2
            #sorted is right half
            if nums[mid] < nums[r] : 
                r = mid
            #sorted is left half so move to unrsorted - 
            elif nums[mid] > nums[r]:
                l = mid +1 


        return nums[l]
        