class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d1 = {}
        d2 = {}
        for n in nums1:
            d1[n] = 1
        for n in nums2:
            d2[n] = 1
        a1 = []
        for n in d1:
            if n not in d2:
                a1.append(n)
        a2 = []
        for n in d2:
            if n not in d1:
                a2.append(n)
        
        return [a1, a2]