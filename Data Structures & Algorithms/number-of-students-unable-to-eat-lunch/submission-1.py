class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d1={}
        d2={}
        for i in students:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for sandwich in sandwiches:
            if d1.get(sandwich, 0) == 0:
                total = 0
                for v in d1.values():
                    total += v
                return total
            d1[sandwich] -= 1
        return 0