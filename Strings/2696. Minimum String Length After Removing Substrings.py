#
def minLength(self, s: str) -> int:
    c=0
    n=len(s)
    f=0
    while f==0:
        for i in range(n-1):
            x=s[i:(i+2)]
            #print('x=', x)
            if x=='AB' or x=='CD':
                s=s[:i]+s[i+2:]
                f=1
                break
        if f==1:
            f=0
        else:
            break
        #print('s_incr=',s)
        
    
    #print('s=',s)
    return len(s)
