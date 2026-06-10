class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left = 0
        su = 0
        re = 0
        for right in range(len(nums)):
            su += nums[right]
            while su > goal and left <= right:
                su -= nums[left]
                left += 1
            temp = left
            temp_su = su
            while temp_su == goal and temp <= right:
                re += 1
                temp_su -= nums[temp]  
                temp += 1
        return re