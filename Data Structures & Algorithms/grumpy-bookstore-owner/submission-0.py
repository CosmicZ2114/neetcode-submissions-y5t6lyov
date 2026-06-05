class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        window_save = sum(customers[i] * grumpy[i] for i in range(minutes))
        best_save = window_save
        for i in range(minutes, n):
            window_save += customers[i] * grumpy[i]          
            window_save -= customers[i - minutes] * grumpy[i - minutes]  
            best_save = max(best_save, window_save)
        return base + best_save