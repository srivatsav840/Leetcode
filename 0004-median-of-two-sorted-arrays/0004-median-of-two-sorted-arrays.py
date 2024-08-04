class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li = sorted(nums1+nums2)
        mid =int(len(li)/2)
        if len(li)%2!=0:
            return float(li[mid])
        else:
            return float((li[mid-1]+li[mid])/2)