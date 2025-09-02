#
def makeSmallestPalindrome(self, s: str) -> str:
    i=0
    j=len(s)-1
    while i<j:
        #print(s[i], s[j])
        if s[i]!=s[j]:
            if ord(s[i]) < ord(s[j]):
                #s[j]=s[i]
                s= s[:j]+s[i]+s[j+1:]
            else:
                #s[i]=s[j]
                s= s[:i]+s[j]+s[i+1:]
                #print('s= ',s)
        i+=1
        j-=1
    #print(s)
    return(s)
