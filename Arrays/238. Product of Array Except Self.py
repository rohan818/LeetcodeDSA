# Product of Array Except Self

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
      length = len(nums)
      result = [0] * length

      result[0] = 1

      for i in range(1, length):
          result[i] = result[i-1] * nums[i-1]

      R = 1

      for i in reversed(range(length)):
          result[i] = result[i] * R
          R  = R * nums[i]

      return result
