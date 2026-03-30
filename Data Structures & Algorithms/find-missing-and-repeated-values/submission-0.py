class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d={}
        n=len(grid)
        a=0
        b=0
        for i in range(n):
            for j in range(n):
                num=grid[i][j]
                if num in d:
                    d[num]+=1
                else:
                    d[num]=1
        for x in range(1,n*n+1):
            if x not in d:
                b=x
            if x in d and d[x] == 2:
                a=x
        return [a,b]