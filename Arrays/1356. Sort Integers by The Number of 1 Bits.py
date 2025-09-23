#
def sortByBits(self, arr: List[int]) -> List[int]:
    
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

    '''def helpsort(n):
        c=0
        while n!=0:
            if (n & 1):
                c+= 1 
            n= n >> 1
        return c
    d={}
    for i in arr:
        x= helpsort(i)
        d[i]=x
    print(d)
    d= dict(sorted(d.items(), key=lambda item: (item[1], item[0])))
    print(d,'*')
    return list(d.keys())
    '''
    
