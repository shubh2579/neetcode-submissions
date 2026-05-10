class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        for i,j in enumerate(nums):
            nums1 = nums.copy()
            res = 1
            nums1.pop(i)
            for i in nums1:
                res *= i
            lst.append(res)
        return lst
        