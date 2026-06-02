class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rot(arr,l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        k=k%len(nums)
        left,right=0,len(nums)-1
        rot(nums,left,right)
        rot(nums,left,k-1)
        rot(nums,k,right)