class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        x = len(pref)
        c = 0
        for w in words:
            if len(w) >= x and w[:x] == pref:
                c += 1
        return c