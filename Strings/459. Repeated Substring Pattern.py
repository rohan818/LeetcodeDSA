#
def repeatedSubstringPattern(self, s: str) -> bool:
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
        # check only those substrings that start at the beginning of the string
            if s[:i] * (n // i) == s:
                return True

    return False
