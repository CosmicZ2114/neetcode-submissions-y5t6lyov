class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        p1=0
        p2=p1+1
        while p1<n-1:
            if nums[p1]==0:
                if nums[p2] != 0:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                p2 += 1
                if p2 >= n:
                    break
            else:
                p1 += 1
                p2 += 1