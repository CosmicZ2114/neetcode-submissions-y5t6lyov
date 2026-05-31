class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d={}
        c=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in d:
            if d[j]==1:
                return -1
            c+=(d[j]+2)//3     # it will always give 1 extra value of the division (ceil function)
        return c
