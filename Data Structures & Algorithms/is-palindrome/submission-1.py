class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i for i in s if ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57)))
        print(s.lower())
        if s.lower() == s[::-1].lower():
            return True
        return False
        