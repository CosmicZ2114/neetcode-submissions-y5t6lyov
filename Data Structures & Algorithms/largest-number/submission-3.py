from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        f=""
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums.sort(key=cmp_to_key(Solution.comp))
        for j in nums:
            f+=j
        if f[0]=="0":
            return "0"
        return f
    @staticmethod
    def comp(s1,s2):
        if s1+s2>s2+s1:
            return -1
        elif s1+s2<s2+s1:
            return 1
        else:
            return 0