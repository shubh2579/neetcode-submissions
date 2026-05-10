class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dct1 = {}
        dct2 = {}

        s = sorted([i for i in s])
        t = sorted([j for j in t])

        for i in s:
            if i in dct1:
                dct1[i] += 1
            else:
                dct1[i] = 1
        for i in t:
            if i in dct2:
                dct2[i] += 1
            else:
                dct2[i] = 1
        
        if dct1 == dct2:
            return True
        return False
        