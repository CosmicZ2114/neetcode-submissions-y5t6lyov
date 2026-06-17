class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,j in enumerate(temperatures):
            while stack and j>temperatures[stack[-1]]:
                y=stack.pop()
                res[y]=i-y
            stack.append(i)
        return res

            