class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r=0
        best = float('inf')
        su = 0
        while r<len(nums):
            su += nums[r]                       
            while su >= target:                  
                best = min(best, r - l + 1)
                su -= nums[l]
                l += 1
            r+=1

        return 0 if best == float('inf') else best