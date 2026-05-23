import heapq
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        heapq.heapify(seats)
        heapq.heapify(students)
        m=0
        for i in range(len(seats)):
            l=heapq.heappop(seats)
            s=heapq.heappop(students)
            d=l-s
            if d<0:
                d=-d
            if s==l:
                m+=0
            else:
                m+=d
        return m
                
                