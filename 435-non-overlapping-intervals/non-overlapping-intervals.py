class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        count = 0 

        for start , end in intervals[1:]:
            if start < res[-1][1]:
                count = count +1
                res[-1][1] = min (end, res[-1][1])
            else :
                res.append([start,end])
        return count 


    

    


        