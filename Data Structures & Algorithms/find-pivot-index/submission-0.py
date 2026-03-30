class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        to=sum(nums)
        ls=0
        for i in range(len(nums)):
            rs=to-ls-nums[i]
            if ls==rs:
               return i
            ls+=nums[i]
        return -1  #solves no pivot case