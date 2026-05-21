class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
    
        mxlen = 0
        left = 0
        uniqset = set()
        for right in range(len(s)):
            # print(right,left)
            while s[right] in uniqset:
                uniqset.remove(s[left])
                left += 1
                
            uniqset.add(s[right])
            # print(uniqset)
            
            cnt = right - left + 1
            if cnt>mxlen:
                mxlen = cnt
        return mxlen

    