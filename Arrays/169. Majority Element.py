#
def majorityElement(self, nums: List[int]) -> int:
    '''
    n = len(nums) // 2
    for i in nums:
        x = sum(1 for j in nums if j == i)
        if x > n:
            return i
    '''

    counts = collections.Counter(nums)
    #print(counts)
    return max(counts.keys(), key=counts.get)
