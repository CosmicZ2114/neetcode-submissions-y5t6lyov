class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ma = float('-inf')
        n = len(nums)
        for i in range(n):
            if i > 0 and i < n - 1:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1] and nums[i] > ma:
                    ma = nums[i]
            elif i == 0:
                if (i == n - 1 or nums[i] > nums[i+1]) and nums[i] > ma:
                    ma = nums[i]
            elif i == n - 1:
                if nums[i] > nums[i-1] and nums[i] > ma:
                    ma = nums[i]
        return nums.index(ma)