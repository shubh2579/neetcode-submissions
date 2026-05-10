class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        lst = []
        for i in nums:
            dct[i] = dct.get(i,0) + 1
        
        dct = sorted(dct.items(),key=lambda item: item[1],reverse=True)
        for i in range(k):
            lst.append(dct[i][0])
        return lst
        