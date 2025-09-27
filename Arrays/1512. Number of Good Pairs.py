#
def numIdenticalPairs(self, nums: List[int]) -> int:
    l=len(nums)
    c=0
    for i in range(0,l-1):
        for j in range(i,l):
            if nums[i]==nums[j] and i<j:
                c+=1
    return c
