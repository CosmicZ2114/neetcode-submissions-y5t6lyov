class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        f = {}
        for n in nums:
            if n in f:
                f[n] += 1
            else:
                f[n] = 1
        arr = nums[:]  
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                f1 = f[arr[j]]
                f2 = f[arr[j+1]]
                if f1 > f2 or (f1 == f2 and arr[j] < arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr