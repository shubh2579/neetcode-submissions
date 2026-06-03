class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        lst = [0 for i in temp]
        stack = [] # This will store the INDICES of the days
        print(temp)
        for i in range(len(temp)):
            print("index: ",i)
            print("list: ", lst)
            # 2. Check if the current day is warmer than the days waiting in the stack
            while stack and temp[i] > temp[stack[-1]]:
                popped_idx = stack.pop()  
                print("popped idx", popped_idx)
                # We found a warmer day for this index!
                lst[popped_idx] = i - popped_idx # Calculate the days distance
                
            # 3. Always push the current day's index onto the stack
            stack.append(i)
            print("stack: ",stack)
                
        return lst 
            