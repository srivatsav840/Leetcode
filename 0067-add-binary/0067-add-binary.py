class Solution:
    def addBinary(self, a: str, b: str) -> str:
        v = int(a,2)
        n = int(b,2)
        s = str(bin(v+n))
        return s[2:]