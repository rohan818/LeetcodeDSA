#
def diStringMatch(self, s: str) -> List[int]:
    low, high = 0, len(s)
    res = []
    for x in s:
        if x == "I":
            res.append(low)
            low += 1
        else:
            res.append(high)
            high -= 1

    return res + [low]
