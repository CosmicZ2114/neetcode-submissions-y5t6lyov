class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d={}
        t=0
        for i in range(len(chars)):
            if chars[i] in d:
                d[chars[i]]+=1
            else:
                d[chars[i]]=1
        for j in range(len(words)):
            w = {}
            for k in words[j]:
                if k in w:
                    w[k] += 1
                else:
                    w[k] = 1
            good = True
            for k in w:
                if k not in d or w[k] > d[k]:
                    good = False
                    break

            if good:
                t += len(words[j])

        return t