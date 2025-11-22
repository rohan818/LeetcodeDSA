#
def bestHand(self, ranks: List[int], suits: List[str]) -> str:
    if len(set(suits))==1:
        return "Flush"
    d={}
    for i in ranks:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    maxi=1
    for i,j in d.items():
        if j>maxi:
            maxi=j
    if maxi>=3:
        return "Three of a Kind"
    elif maxi==2:
        return "Pair"
    else:
        return "High Card"
