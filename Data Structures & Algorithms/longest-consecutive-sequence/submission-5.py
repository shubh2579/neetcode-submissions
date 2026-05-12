class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        num_set = set(nums)
        print(num_set)
        
        max_streak = 0
        
        for num in num_set:
            # print("num", num)
            if  (num-1) not in num_set:
                current_num = num
                current_streak = 1
                while (current_num + 1) in num_set:
                    current_streak += 1
                    current_num += 1
                # print(current_streak, max_streak)
                max_streak = max(max_streak, current_streak)
        
        return max_streak
            