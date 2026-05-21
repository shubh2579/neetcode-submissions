class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        mxlen = 0
        for i in range(len(s)):
            uniqset = set(s[i])
            cnt = 0
            for j in range(i+1, len(s)):
                if s[j] not in uniqset:
                    uniqset.add(s[j])
                    cnt  = len(uniqset)
                    if cnt > mxlen:
                        mxlen = cnt
                else:
                    cnt  = len(uniqset)
                    if cnt > mxlen:
                        mxlen = cnt
                    break
                    
                
        return mxlen

        