class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        r = 0 
        l = 0 
        output = [ ] 
        while r < len(nums) : 
            while q and nums[r] > nums[q[-1] ]:
                q.pop()
            q.append(r)
            if r-l+1 ==  k : 
                output.append(nums[q[0]])
                l=l+1
            if l > q[0] : 
                q.popleft()
            r = r + 1
        return output 


        