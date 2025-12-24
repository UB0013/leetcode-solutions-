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
            dist, x, y = (heapq.heappop(heap))
            k = k-1
            res.append([x,y])
        # for dist,x, y in res : 
        #     ans.append([x,y])
        return res 
        
        