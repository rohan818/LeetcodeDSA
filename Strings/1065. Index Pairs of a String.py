# Index Pairs of a String
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []

        for i in range(len(text)):
            for j in range(len(text)):
                if text[i:j+1] in words:
                    res.append([i,j])
        return res
