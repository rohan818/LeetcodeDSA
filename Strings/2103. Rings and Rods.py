#
class Solution:
    def countPoints(self, rings: str) -> int:
        res = 0
        for i in range(10):
            i = str(i)
            if 'R'+i in rings and 'G'+i in rings and 'B'+i in rings:
                res += 1
        return res
