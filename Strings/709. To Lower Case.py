#
class Solution:
    def toLowerCase(self, s: str) -> str:
        u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l = 'abcdefghijklmnopqrstuvwxyz'

        d = dict(zip(u, l))

        return ''.join(d[x] if x in d else x for x in s)
