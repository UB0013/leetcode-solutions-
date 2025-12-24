class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        res = []
        for x ,y in points : 
            dist = x*x + y*y
            heap.append ([dist,x,y])
        heapq.heapify(heap)
        
        while k > 0 :
            res.append(heapq.heappop(heap))
            k = k-1
        for dist , x, y in res : 
            ans.append([x,y])
        return ans 
        
        