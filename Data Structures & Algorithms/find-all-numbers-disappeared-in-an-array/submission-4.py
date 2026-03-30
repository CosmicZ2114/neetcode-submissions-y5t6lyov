class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m=len(nums)
        x=[]
        for i in range(1,m+1):
            if i not in  nums:
                x.append(i)
        return x