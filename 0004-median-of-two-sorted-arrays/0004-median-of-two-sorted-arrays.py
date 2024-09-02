class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li = sorted(nums1+nums2)
        if len(li)%2 !=0:
            return float(li[int((len(li)/2))])
        else:
            v = int(len(li)/2)
            s =v-1
            return float((li[s]+li[v])/2)