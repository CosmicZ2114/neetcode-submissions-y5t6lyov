class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i=0
        j=0
        summ={}
        n=len(nums)
        while i < n:
            if i < n-1 and nums[i] < nums[i+1]:
                i += 1
            else:
                summ[str(nums[j:i+1])] = sum(nums[j:i+1])  
                i += 1
                j = i
        mxx= max(summ.values())
        return mxx