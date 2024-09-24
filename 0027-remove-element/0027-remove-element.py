class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v = len(nums)
        t=0
        for i in range(v):
            if nums[i]!=val:
                i+=1
                nums.insert(0,nums[i-1])
                del nums[i]
            else:
                t+=1
        return (v-t)
                