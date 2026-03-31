class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        r=0
        for j in d.values():
                r += (j * (j - 1)) // 2
        return r