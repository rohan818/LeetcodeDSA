#
def buildArray(self, nums: List[int]) -> List[int]:
    n=len(nums)
    r=[]
    for i in range(n):
        r.append(nums[nums[i]])
    return r
