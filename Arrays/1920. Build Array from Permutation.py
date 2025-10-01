#
def buildArray(self, nums: List[int]) -> List[int]:
    n=len(nums)
    r=[]
    for i in range(n):
        r.append(nums[nums[i]])
    return r

'''
from typing import List

def buildArray(self, nums: List[int]) -> List[int]:
    return [nums[nums[i]] for i in range(len(nums))]

'''
