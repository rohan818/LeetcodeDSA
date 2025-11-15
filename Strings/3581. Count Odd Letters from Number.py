#
def countOddLetters(self, n: int) -> int:
    lookup = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
    }

    s = ""
    for x in str(n):
        s += lookup[x]

    c = Counter(s)
    ans = 0
    for val in c.values():
        ans += val%2

    return ans
