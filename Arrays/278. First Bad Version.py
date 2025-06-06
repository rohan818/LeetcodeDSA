#
class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = n
        l, r = 1, res
        while l <= r:
            m = (l + r)//2
            if isBadVersion(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
