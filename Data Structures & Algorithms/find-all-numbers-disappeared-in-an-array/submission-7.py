class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = len(nums)
        x = []
        nums_set = set(nums)        
        for i in range(1, m+1):
            if i not in nums_set:   
                x.append(i)
        return x