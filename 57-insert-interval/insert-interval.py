class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ni = newInterval 
        res =[]
        for i in range(len(intervals)) :
            if ni[1] < intervals[i][0] :
                res.append(ni)
                return res + (intervals[i:])
            elif ni[0] > intervals[i][1]:
                res.append(intervals[i])
            else :
                ni =  [ min (ni[0],intervals[i][0]) , max(ni[1],intervals[i][1])]
        res.append(ni)
        return res 

        