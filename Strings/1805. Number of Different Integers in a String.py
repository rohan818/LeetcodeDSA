#
def numDifferentIntegers(self, word: str) -> int:
    s = ""
    for i in word:
        if i.isdigit():
            s += i
        else:
            s += " "
    return len(set(str(int(x)) for x in s.split() if x))
