class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nu=sorted(nums)
        n=len(nu)
        mx_dif= (nu[n-2]*nu[n-1])-(nu[0]*nu[1])
        return mx_dif