class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d = {}
        r=0
        for i in allowed:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for word in words:
            w = {}
            for k in word:
                if k in w:
                    w[k] += 1
                else:
                    w[k] = 1
            good = True
            for x in w:
                if x not in d:
                    good = False
                    break
            if good:
                r+=1

        return r