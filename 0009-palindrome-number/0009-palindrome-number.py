class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            num = x
            rev = 0
            while num>0:
                a = num%10
                rev = rev*10+a
                num = num//10
            return x == rev

v = Solution()
print(v.isPalindrome)
