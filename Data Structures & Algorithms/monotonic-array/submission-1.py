class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i=True
        d=True
        n=len(nums)
        for j in range(n-1):
            if nums[j]>nums[j+1]:
                i=False
            if nums[j]<nums[j+1]:
                d=False
        return i or d