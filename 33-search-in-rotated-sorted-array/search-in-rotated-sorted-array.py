class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

      
        while l <=r : 
            
            mid = (l+r)//2

            if target == nums[mid]:
                return mid 

            # from this poit it is guaranteed that target != nums of mid 


            # right is sorted 
            if nums[mid]<=  nums[r]:
                # target found  in right 
                if nums[mid] < target <=nums[r] : 
                    l = mid +1
                else : #target in left discard right 
                    r = mid-1
            #left is sorted check in left 
            else:
                if nums[mid] > target >= nums[l]:
                    r = mid -1
                else : #not found in left discard left 
                    l =mid+1
        return -1 

            
 
 
        