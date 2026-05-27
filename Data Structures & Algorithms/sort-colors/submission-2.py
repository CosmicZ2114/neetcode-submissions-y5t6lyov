class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        x=0
        def swap(y, z):
            temp = nums[y]
            nums[y] = nums[z]
            nums[z] = temp
        while x<=right:
            if nums[x]==0:
                swap(left,x)
                left+=1
            elif nums[x]==2:
                swap(x,right)
                right-=1
                x-=1    # for re-examination of the swapped element
            x+=1