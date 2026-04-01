class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num3=set(nums1)
        num4=set(nums2)
        arr=[]
        for num in num3:
            if num in num4:
                arr.append(num)
        return arr
        