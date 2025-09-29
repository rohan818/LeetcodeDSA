# Missing Number In Arithmetic Progression
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        
        if d == 0:
            return arr[0]
        #
        for i in range(1, len(arr)):
            if arr[i-1] + d != arr[i]:
                return arr[i-1] + d
