class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele ,counter =None,0
        for i in nums:
            if counter ==0:
                ele = i
            if i == ele:
                counter+=1
            else:
                counter-=1
                
        return ele