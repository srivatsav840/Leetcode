class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        li =[]
        while columnNumber>0:
            columnNumber-=1
            rem = columnNumber%26
            li.append(chr(65+rem))
            columnNumber //=26
            
        return ''.join(li[::-1])