class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in range(len(nums)):
            if (nums[i] in hash) and (abs(i-hash[nums[i]]) <= k):
                return True
            hash[nums[i]] = i
        return False
        '''        
        num_dict = {}
        for i in nums:
            if i in num_dict:
                return True
            else:
                num_dict[i] = 1
        
        return False
        num_dict = {}
        '''
