class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        v =""
        for i in digits:
            v+=str(i)
        nums = str(int(v)+1)
        
        return list(map(int,nums))
                