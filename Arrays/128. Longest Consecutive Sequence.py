# Longest Consecutive Sequence

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
      
      n = len(nums)
      if n == 0:
          return 0
      nums.sort()

      res = 1
      c = 1

      for i in range(1, n):
          if nums[i] != nums[i-1]:
              if nums[i] - nums[i-1] ==1:
                  c += 1
              else:
                  res = max(res, c)
                  c = 1
          # print(i, c)
      return max(res, c)
