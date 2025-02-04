# 1085
class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = min(nums)
        s = 0
        while min_num > 0:
            s += min_num % 10
            min_num //= 10
        return 1 if s % 2 == 0 else 0
