class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=k-1
        md=1000
        while r<len(nums):
            g=nums[r]-nums[l]
            if g<md:
                md=g
            l+=1
            r+=1
        return md
