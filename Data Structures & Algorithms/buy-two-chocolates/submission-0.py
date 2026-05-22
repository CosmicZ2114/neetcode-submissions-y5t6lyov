class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        buy=prices[0]+prices[1]
        if money>=buy:
           return money -(prices[0]+prices[1])
        else:
            return money