#
def pivotIndex(self, nums: List[int]) -> int:
    x=len(nums)
    cur= 0
    total= sum(nums)
    for i in range(x):
        cur+= nums[i]
        if cur -  nums[i] == total- cur:
            return i
    return -1
