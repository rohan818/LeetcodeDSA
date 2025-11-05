#
def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    res = []
    n = len(words)
    for i in range(n):
        if x in words[i]:
            res.append(i)
    return res

    #return [i for i, w in enumerate(words) if x in w]
