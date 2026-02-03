class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res =[]
        digitchar = {"2" : "abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8" :"tuv",
        "9" : "wxyz"}

        curr = []
      

        def dfs (curr,i):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return 
            for c in digitchar[digits[i]]:
                curr.append(c)
                dfs (curr,i+1)
                curr.pop()
        dfs (curr,0)
        return res 

        