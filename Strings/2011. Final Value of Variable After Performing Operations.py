#
def finalValueAfterOperations(self, operations: List[str]) -> int:
    x=0
    for i in operations:
        if '+' in i:
            x+=1
            continue
        if '-' in i:
            x-=1
            continue
    return x
