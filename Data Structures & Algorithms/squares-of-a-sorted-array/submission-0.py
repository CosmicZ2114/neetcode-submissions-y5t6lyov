class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        arr=[]
        while l<=r:
            if (nums[l])**2 >(nums[r])**2:
                arr.append(nums[l]**2)
                l+=1
            else:
                arr.append(nums[r]**2)
                r-=1
        return arr[::-1]