# Goat Latin
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        for i, word in enumerate(sentence.split()):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[0]
            res.append(word + 'ma' + 'a'*(i+1))
        
        return " ".join(res)
