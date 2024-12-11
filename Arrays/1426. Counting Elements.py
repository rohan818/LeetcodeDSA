# Counting Elements
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        hashset = set(arr)
        for x in arr:
            if x + 1 in hashset:
                count += 1
        return count
