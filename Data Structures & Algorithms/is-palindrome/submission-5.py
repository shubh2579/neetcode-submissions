class Solution:
    def isPalindrome(self, s: str) -> bool:
        # These two variables are our only extra space usage
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move left pointer until it hits a valid character
            if not s[l].isalnum():
                l += 1
            # Move right pointer until it hits a valid character
            elif not s[r].isalnum():
                r -= 1
            # Now both are on alphanumeric characters
            else:
                if s[l].lower() != s[r].lower():
                    return False # Stop early!
                l += 1
                r -= 1
                
        return True
        