# code 1394
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        l = -1
        for n, count in d.items():
            if n == count:
                l = max(l, n)
        return l
