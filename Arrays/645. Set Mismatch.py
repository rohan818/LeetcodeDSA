# 645. Set Mismatch

def findErrorNums(self, nums: List[int]) -> List[int]:
      n = len(nums)
      nums = sorted(nums)
      dup, missing = -1, 1
      for i in range(1, n):
          if nums[i] == nums[i-1]:
              dup = nums[i]
          elif nums[i] > nums[i-1] + 1:
              missing = nums[i-1] + 1
      if nums[n-1] != n:
          return [dup, n]
      else:
          return [dup, missing]
