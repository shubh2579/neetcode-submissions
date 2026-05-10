class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={}

        for i,n in enumerate(nums):
            dct[n] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in dct and i != dct[diff]:
                return[i, dct[diff]]


        
        