class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged =""
        l =0
        r =0
        while l<len(word1) and r <len(word2):
            merged+=word1[l]
            merged +=word2[r]
            l+=1
            r+=1
            
        while l<len(word1):
            merged+=word1[l]
            l+=1
        while r<len(word2):
            merged+=word2[r]
            r+=1
            
        return merged