#
def findClosestNumber(self, nums: List[int]) -> int:
    ans=float('inf')
    for num in nums:
        ans=min(abs(num),ans) 
    return ans if ans in nums else -ans
