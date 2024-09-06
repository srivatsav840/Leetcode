class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic ={}
        for index,num in enumerate(nums):
            comp = target-num
            if comp in dic:
                return [dic[comp],index]
            else:
                dic[num]=index