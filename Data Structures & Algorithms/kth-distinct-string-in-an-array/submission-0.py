class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1  
            i += 1
        
        c = 0
        for ke in d:
            if d[ke] == 1:
                c += 1
                if c == k:  
                    return ke
        
        return ""