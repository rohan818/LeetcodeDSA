#
def thirdMax(self, nums: List[int]) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums)
    else:
        return nums[2]
