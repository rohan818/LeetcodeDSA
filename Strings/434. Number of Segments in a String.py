#
def countSegments(self, s: str) -> int:
    
    # conditions: for i th character, it should not be a space && 
    # it can either be first character or character before  i th one is a space

    return sum(s[i] != ' ' and (i == 0 or s[i-1] == ' ') for i in range(len(s)))
