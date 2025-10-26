# Index Pairs of a String
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []

        for i in range(len(text)):
            for j in range(len(text)):
                if text[i:j+1] in words:
                    res.append([i,j])
        return res

    '''
    res = []
    
        for word in words:
            start = 0
            while start < len(text):
                index = text.find(word, start)
                if index == -1:
                    break
                res.append([index, index + len(word) - 1])
                start = index + 1
    
        return sorted(res)
    '''
