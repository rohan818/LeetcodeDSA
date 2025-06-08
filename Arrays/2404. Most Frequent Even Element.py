#
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        d = {}

        for i in nums:
            if i in d and i%2==0:
                d[i] += 1
            elif i not in d and i%2==0:
                d[i] = 1
        if len(d)==0:
            return -1
        res = max(d, key=lambda x:d[x])
        return res
