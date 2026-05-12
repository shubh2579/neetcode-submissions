class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums = sorted(list(set(nums)))
        # print(nums)
        i = 0
        cnt = 0
        mx_cnt = 0
        while i+1 < len(nums):
            
            if nums[i+1] - nums[i] ==1:
                cnt += 1
                if cnt > mx_cnt:
                    mx_cnt = cnt
                i+=1
                # print(cnt)
                # mx_cnt = cnt
            else:
                if cnt > mx_cnt:
                    mx_cnt = cnt
                    # print(mx_cnt)
                    cnt = 0
                    i+=1
                else:
                    cnt=0
                    i+=1
                    continue
        return mx_cnt + 1
        