# Maximum Product of Three Numbers
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        max_product1 = nums[-1] * nums[-2] * nums[-3]

        max_product2 = nums[0] * nums[1] * nums[-1]

        return max(max_product1, max_product2)
