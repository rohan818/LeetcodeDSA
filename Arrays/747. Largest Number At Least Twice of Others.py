# Largest Number At Least Twice of Others
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        for i in nums:
            if all(m >= 2*x for x in nums if x!=m):
                return nums.index(m)
        return -1
