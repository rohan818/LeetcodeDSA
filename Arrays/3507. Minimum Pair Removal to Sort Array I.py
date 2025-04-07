# Minimum Pair Removal to Sort Array I

import sys
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0
        
        c = 0
        while nums != sorted(nums):
            minSum = sys.maxsize
            minIndices = [0, 0]
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] < minSum:
                    minSum = nums[i]+nums[i+1]
                    minIndices[0] = i
                    minIndices[1] = i+1
            nums[minIndices[0]] = nums[minIndices[0]] + nums[minIndices[1]]
            nums.pop(minIndices[1])
            c += 1
        return c
                
