class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr=[]
        d={}
        for i in numbers:
                x=target-i
                if x in numbers:
                    d[i]=(x,numbers.index(x)+1)
        for j in d:
            y=numbers.index(j)+1
            x=d[j][1]
            if y<x:
                arr=[y,x]
        return arr