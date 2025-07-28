#
def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = w2  = -1
        d = n = len(wordsDict)
        for i in range(n):
            if wordsDict[i] == word1:
                w1 = i
            elif wordsDict[i] == word2:
                w2 = i
            
            if w1 != -1 and w2 != -1:
                d = min(d, abs(w1 - w2))

        return d
