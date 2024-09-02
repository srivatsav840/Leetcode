class Solution:
    def reverse(self, x: int) -> int:
        s =str(x)
        if x<0:
            v =int(s[len(s):0:-1])
            if v>=2**31 or v<(-2**31):
                return 0
            return -v
        else:
            v =str(s[::-1])
            if int(v)>=(2**31)-1 or int(v)<(-2**31):
                return 0
            return int(v)
            
    