class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        pref =""
        if not strs:
            return pref
        for i in range(len(s)):
            for string in strs:
                if i>=len(string) or s[i]!=string[i]:
                    return pref
            pref+=s[i]
        return pref    
              
