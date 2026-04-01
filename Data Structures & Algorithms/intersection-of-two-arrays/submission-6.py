class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for i in nums1:
            if i in nums2:
                arr.append(i)
        arr=set(arr)
        arr=list(arr)
        return arr