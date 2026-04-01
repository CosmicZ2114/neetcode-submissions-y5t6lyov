class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a1 = []
        a2 = []
        for n in nums1:
            if n not in nums2 and n not in a1:
                a1.append(n)
        for n in nums2:
            if n not in nums1 and n not in a2:
                a2.append(n)

        return [a1, a2]