class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        v= nums.count(0)
        s = nums.count(1)
        nums  +=[0]*v
        nums +=[1]*s
        nums+=[2]*(le-int(v+s))
        del nums[:le]
        return nums
            
            