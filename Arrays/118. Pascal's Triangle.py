#
def generate(self, numRows: int) -> List[List[int]]:
    if numRows==1:
        return [[1]]
    elif numRows==2:
        return [[1],[1,1]]
    l=[[1],[1,1]]
    for i in range(2, numRows):
        x=[1]
        for  j in range(i-1):
            x.append(l[i-1][j]+l[i-1][j+1])
        x.append(1)
        l.append(x)
    return l
