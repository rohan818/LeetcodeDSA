#
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res, track = 0, 0
        for c in s:
            if c == 'R':
                track += 1
            else:
                track -= 1
            res += int(track == 0)
        return res
