# Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        d= {}
        for i in nums1:
            d[i] = d.get(i, 0) + 1
        r = []
        for i in nums2:
            if i in d and d[i]>0:
                r.append(i)
                d[i] -= 1
        return r
