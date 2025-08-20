class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        s = s.split()
        d=  {}
        n = len(pattern)
        f = 0
        for i in range(n):
            if pattern[i] in d:
                if d[pattern[i]] == s[i]:
                    continue
                else:
                    print(s[i])
                    f = 1
                    break
            else:
                d[pattern[i]] = s[i]
        if f == 1:
            return False
        return True
        '''
        map_char = {}
        map_word = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True 




