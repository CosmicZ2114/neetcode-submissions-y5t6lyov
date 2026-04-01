class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        n=len(nums1)
        for i in range(n):
            if nums1[i] in nums2:
                if nums1[i]  not in arr:
                    arr.append(nums1[i])
        return arr