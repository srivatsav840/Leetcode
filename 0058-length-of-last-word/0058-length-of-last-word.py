class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        v = list(map(str,s.split()))
        return len(v[-1])
        
            
            
                
                
            
            