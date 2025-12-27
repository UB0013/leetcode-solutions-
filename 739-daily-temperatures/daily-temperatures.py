class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        res = [0]*(len(temperatures))
     
        
        for i, t in enumerate(temperatures): 
            while stack and stack[-1][0] < t: 
                temp, index =  stack.pop()
                res[index] = (i-index)
            stack.append([t,i])
        return res 

72-5

#t= 72

# [75-2,71-3, ]

# t = 73
# index = 0 
          
# res = [1,1,1,2]

        