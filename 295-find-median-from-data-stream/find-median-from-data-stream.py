class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify_max(self.maxheap)
        

    def addNum(self, num: int) -> None:
        if self.maxheap and self.maxheap[0]< num :
            heapq.heappush(self.minheap,num)
        else :
            heapq.heappush_max(self.maxheap,num)
        if len(self.maxheap) > len (self.minheap)+1:
            heapq.heappush(self.minheap,heapq.heappop_max(self.maxheap))
        if len(self.minheap)> len(self.maxheap)+1:
            heapq.heappush_max(self.maxheap, heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        elif len(self.maxheap) < len(self.minheap):
            return self.minheap[0]
        else :
            return (self.maxheap[0]+self.minheap[0])/2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()