class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        #lightest with heaviest 
        #left lightest
        #right heaviest 
        #increment boat count  count <=
        #limit ecxceeds heaviest is the bottle next send him alone incereament boat count 
        people.sort()
        print (people)
        l = 0 
        r = len(people)-1
        boat = 0 

        while l<= r: 
            if people[l] + people[r] <= limit :
                boat +=1 
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                boat +=1 
                r -= 1 
            elif l == r : 
                boat +1 
                l+=1
        return boat











        