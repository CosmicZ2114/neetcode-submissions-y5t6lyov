class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c=0
        ex=sorted(heights)
        i=0
        n=len(heights)
        while i<n:
            if heights[i] != ex[i]:
                c+=1
            i+=1
        return c