class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d={}
        n=len(nums)
        pa=n//2
        for i in range(n):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]]=1
        for k in d.values():
            if k%2 ==1:
                return False
        return True