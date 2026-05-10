class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        s=1
        P = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                pro = prices[s] - prices[b]
                P = max(P, pro)
            else:
                b = s
            s += 1
        return P