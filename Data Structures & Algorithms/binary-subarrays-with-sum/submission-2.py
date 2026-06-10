class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            left = 0
            su = 0
            re = 0
            for right in range(len(nums)):
                su += nums[right]
                while su > k:
                    su -= nums[left]
                    left += 1
                re += right - left + 1  
            return re

        return atMost(goal) - atMost(goal - 1)