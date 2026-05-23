class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        mxlen = 0
        counts = {}
        
        for right in range(len(s)):
            
            if s[right] in counts:
                counts[s[right]] += 1
            else:
                counts[s[right]] = 1
            window = right-left+1
            
            mx_freq = counts[max(counts, key=counts.get)]
            replacement = window - mx_freq
            if replacement <=k:
                mxlen += 1
            else:
                counts[s[left]] -= 1
                left += 1
                
        return mxlen
            
        