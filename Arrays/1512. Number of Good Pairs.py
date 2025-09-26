#
def numIdenticalPairs(self, nums: List[int]) -> int:
    l=len(nums)
    c=0
    for i in range(0,l-1):
        for j in range(i,l):
           #print(i,nums[i],j,nums[j])
            if nums[i]==nums[j] and i<j:
                #print('*')
                c+=1
    return c
