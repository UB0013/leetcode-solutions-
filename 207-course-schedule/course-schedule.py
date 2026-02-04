class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i : [] for i in range ((numCourses))}
        visit = set ()

        for element  in prerequisites:
            crs = element[0]
            pre = element[1]
            premap[crs].append(pre)
        print(premap)

        def dfs (crs) :
            if crs in visit :
                return False 
            if premap[crs] == []:
                return True 
            visit.add(crs)
            for pre in premap[crs]:
                if dfs (pre) == False :
                    return False 
                premap[crs] = []
            visit.remove (crs)
            return True

        for crs in range (numCourses) : 
            if dfs (crs) == False :
                return False 
        return True 



        