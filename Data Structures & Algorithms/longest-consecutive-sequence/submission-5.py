class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r = set(nums)
        l = list(r)
        d = {}
        ree = []

        for i in l:
            if i - 1 not in r:          
                length = 1
                while i + length in r:
                    length += 1
                d[i] = length           

        for j in d:
            ree.append(d[j])            

        if len(ree) == 0:
            return 0
        else:
            return max(ree)