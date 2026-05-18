class Solution:
    def trap(self, height: List[int]) -> int:
        maxright = []
        maxleft = []
        
        for i in range(len(height)):
            maxleft.append(max(height[:i+1]))
        for i in range(len(height)):
            # print(max(height[i],height[i:]))
            maxright.append(max(height[i:]))
        wtr = 0    
        for current,left,right in zip(height,maxleft, maxright):
            trapped = min(right,left) - current
            wtr += trapped
        
        return wtr
        