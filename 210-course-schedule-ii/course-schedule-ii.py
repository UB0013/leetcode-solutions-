class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i :[] for i in range (numCourses)}
        visit = set ()
        done = set ()
        output = []

        for crs , pre in prerequisites:
            premap[crs].append(pre)
        print(premap)

        
        def dfs (crs) :
            if crs in visit :
                return False 
            if crs in done :
                return True
            visit.add(crs)
            for pre in premap[crs]:
                if dfs (pre) == False :
                    return False
            done.add(crs)
            output.append(crs)
            visit.remove(crs)
            return True 


        for crs in range(numCourses) :
            if dfs(crs) == False :
                return [] 

        return output  

        