class Solution:
    def longestPalindrome(self, s: str) -> str:
        lon =""
        if len(s)==1:
            return s
        for i in range(len(s)):
            res = s[i]
            for j in range(i+1,len(s)):
                res +=s[j]
                if res ==res[::-1]:
                    if len(res)>len(lon):
                        lon = res
                    

        if lon:
            return lon
        return res[0]