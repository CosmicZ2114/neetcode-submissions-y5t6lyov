class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rs=[1]*len(nums)
        pre=1
        for i in range(len(nums)):  #travel left to right
            rs[i]=pre
            pre*=nums[i]
        po=1
        for i in range(len(nums)-1,-1,-1):  #travel right to left
            rs[i]*=po
            po*=nums[i]
        return rs