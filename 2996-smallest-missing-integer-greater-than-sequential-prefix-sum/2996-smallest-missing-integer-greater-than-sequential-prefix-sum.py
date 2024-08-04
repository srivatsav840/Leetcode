class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        lon=0
        v =nums[0]
        for i in nums:
            if i == v:
                v =i+1
                lon+=i
            else:
                break
        if lon not in nums:
            return lon
        else:
            for i in range(len(nums)):
                if lon+1 not in nums:
                    return lon+1
                else:
                    lon+=1
                