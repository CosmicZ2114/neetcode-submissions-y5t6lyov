class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        r=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=len(nums)//3
        for j in d:
            if d[j]>l:
                r.append(j)
        return r