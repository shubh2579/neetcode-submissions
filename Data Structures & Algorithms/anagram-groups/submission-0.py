class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dct = {}
        for st in strs:
            print(sorted(st))
            key = "".join(sorted(st))
            if key in dct:
                dct[key].append(st)
            else:
                dct[key] = [st]
        return list(dct.values())
        