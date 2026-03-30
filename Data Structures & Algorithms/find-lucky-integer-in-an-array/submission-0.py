class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        n=len(arr)
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        gl=0
        for k in d:
            if d[k]==k:
                if gl<k:
                    gl=k
        if gl==0:
            return -1
        else:
            return gl