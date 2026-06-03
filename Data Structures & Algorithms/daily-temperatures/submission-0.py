class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        lst = []
        for i in range(len(temp)):
            res = 0
            for j in range(i+1, len(temp)):
                if temp[j]>temp[i]:
                    res = j-i
                    break
            lst.append(res)
                
        return lst
        