class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        c=0
        while l<=r:
            su=people[l]+people[r]
            if su<=limit:
                c+=1
                l+=1
                r-=1
            elif su>limit:
                if people[r]>limit:
                    r-=1
                else:
                    c+=1
                    r-=1
            
        return c