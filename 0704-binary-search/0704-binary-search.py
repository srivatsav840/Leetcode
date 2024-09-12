class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left =0
        right=len(nums)-1

        def searching(left,right,nums):
            if left>right:
                return -1
            mid =(left+right)//2
            if nums[mid]==target:
                return mid 
            if target>nums[mid]:
                return searching(mid+1,right,nums)
            else:
                return searching(left,mid-1,nums)
        return searching(left,right,nums)