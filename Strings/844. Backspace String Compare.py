#
def backspaceCompare(self, s: str, t: str) -> bool:
    def build(s):
        res = []
        for c in s:
            if c != '#':
                res.append(c)
            elif res:
                res.pop()
        return ''.join(res)
    
    return build(s) == build(t)
