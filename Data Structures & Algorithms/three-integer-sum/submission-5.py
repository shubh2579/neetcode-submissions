class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        lst = []
        for first in range(len(nums)-2):
            left = first+1
            right = len(nums)-1
            if first > 0 and nums[first] == nums[first-1]:
                continue
            while left < right:
                # print(nums[left] + nums[right], -nums[first])
                if nums[left] + nums[right] == -nums[first]:
                    lst.append([nums[first], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    # Keep skipping as long as the next element is a duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < -nums[first]:
                    left += 1
                    
                else:
                    right -= 1
        return lst

            