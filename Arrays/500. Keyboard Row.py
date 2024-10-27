#500. Keyboard Row

def findWords(self, words: List[str]) -> List[str]:
    set1, set2, set3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    valid_words = []
    for word in words:
        w = set(word.lower())
        if w <= set1 or w <= set2 or w <= set3:
            valid_words.append(word)
    return valid_words
