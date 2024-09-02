class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0:]==s[::-1]:
            return True
        else:
            return False