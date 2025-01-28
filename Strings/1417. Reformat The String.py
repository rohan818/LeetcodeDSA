# Reformat The String
class Solution:
    def reformat(self, s: str) -> str:
        a = [i for i in s if i.isalpha()]
        d = [i for i in s if i.isdigit()]
        if len(a) < len(d):
            a, d = d, a
        if len(a) - len(d) > 1:
            return ""
        
        res = []
        while a:
            res.append(a.pop())
            if d:
                res.append(d.pop())
        return "".join(res)
