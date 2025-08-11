#
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    hash = {}
    for i in range(len(nums)):
        if (nums[i] in hash) and (abs(i-hash[nums[i]]) <= k):
            return True
        hash[nums[i]] = i
    return False
            
