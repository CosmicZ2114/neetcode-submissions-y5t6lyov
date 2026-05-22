import heapq
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)               
        min1 = heapq.heappop(prices)        
        min2 = heapq.heappop(prices)        
        buy=min1 + min2
        if money>=buy:
           return money -buy
        else:
            return money