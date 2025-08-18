#
def isIsomorphic(self, s: str, t: str) -> bool:
    d={}
    hset = set()
    l=len(s)
    for i in range(l):
        if s[i] not in d:
            if t[i] in hset:
                return False
            d[s[i]] = t[i]
            hset.add(t[i])
        else:
            if t[i] != d[s[i]]:
                return False
    return True
    
