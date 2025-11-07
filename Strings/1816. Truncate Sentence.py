#
def truncateSentence(self, s: str, k: int) -> str:
    words = s.split()
    res = words[:k]
    return ' '.join(res)
