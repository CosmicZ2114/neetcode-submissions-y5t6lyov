class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        check={}
        for person in range(1, n + 1):
            check[person] = {"tru": 0, "betru": 0}

        for i in trust:
            check[i[0]]["tru"] += 1     
            check[i[1]]["betru"] += 1    

        for person in range(1, n + 1):
            if check[person]["tru"] == 0 and check[person]["betru"] == n - 1:
                return person

        return -1